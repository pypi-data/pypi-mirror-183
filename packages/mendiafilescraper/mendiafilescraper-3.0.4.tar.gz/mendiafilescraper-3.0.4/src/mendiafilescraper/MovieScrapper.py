import datetime
import logging
import multiprocessing
import os
import re
import time
from enum import Enum
from pathlib import Path
from typing import List, Optional, Tuple

import tmdbsimple as tmdb
from pymediainfo import MediaInfo

from mendiafilescraper.Database import Movies, database
from mendiafilescraper.Hasher import Hasher
from mendiafilescraper.Mendia import Movie, publish_movies
from mendiafilescraper.PathElement import FileObject, PathElement, PathObject


class MovieScrapper:
    @staticmethod
    def parse_media_info(path: str):

        try:
            media_info = MediaInfo.parse(
                filename=path,
                full=True,
                parse_speed=0.1,
            )
        except Exception:
            logging.exception("Failed to parse media info for '%s'", path)
            return -1, None, None, None, None, None

        bitrate = 0
        codec = "unknown"
        dynamic_range = "SDR"
        resolution = "unknown"
        audio_languages = []
        subtitle_languages = []
        found_video = False

        class HDRType(Enum):
            DOLBY_VISION = 0
            HDR10 = 1
            HDR10Plus = 2
            NONE = 3

        hdr_type = HDRType.NONE

        for track in media_info.tracks:
            if not found_video and track.track_type == "Video":
                hdr_data = []
                for entry in dir(track):
                    if entry.startswith("hdr_format"):
                        hdr_data.append(track.__getattribute__(entry))
                found_video = True

                # Dolby Vision profile strings
                dolby_vision_profile_strings = [
                    "dvhe.04",
                    "dvhe.05",
                    "dvhe.07",
                    "hev1.08",
                    "avc3.09",
                ]

                for hdat in hdr_data:
                    hdat_string = str(hdat)
                    hdat_string_lower = hdat_string.lower()
                    # See if it is Dolby Vision with profile strings
                    for profile_string in dolby_vision_profile_strings:
                        if profile_string in hdat_string:
                            hdr_type = HDRType.DOLBY_VISION
                            break
                    # See if it is Dolby Vision by name
                    if "dolby" in hdat_string_lower or "vision" in hdat_string_lower:
                        hdr_type = HDRType.DOLBY_VISION
                    if hdr_type == HDRType.DOLBY_VISION:
                        break
                    # See if it is HDR10Plus
                    if (
                        "hdr10+" in hdat_string_lower
                        or "hdr10plus" in hdat_string_lower
                    ):
                        hdr_type = HDRType.HDR10Plus
                    # Must be HDR10 then
                    if hdr_type == HDRType.NONE:
                        hdr_type = HDRType.HDR10

                if hdr_type == HDRType.DOLBY_VISION:
                    dynamic_range = "HDR / Dolby Vision"
                elif hdr_type == HDRType.HDR10Plus:
                    dynamic_range = "HDR / HDR10+"
                elif hdr_type == HDRType.DOLBY_VISION:
                    dynamic_range = "HDR / HDR10"
                else:
                    # Reset back to SDR if the format is none of the three
                    dynamic_range = "SDR"

                if track.bit_rate is not None:
                    bitrate = track.bit_rate
                elif (
                    track.bit_rate_mode == "VBR" and track.maximum_bit_rate is not None
                ):
                    bitrate = track.maximum_bit_rate

                if track.format is not None:
                    codec = track.format

                if track.width is not None and track.height is not None:
                    resolution = f"{track.width}x{track.height}"
            elif track.track_type == "Audio":
                if track.language is None:
                    audio_languages.append("unknown")
                else:
                    audio_languages.append(track.language)
            elif track.track_type == "Text":
                if track.language is None:
                    subtitle_languages.append("unknown")
                else:
                    subtitle_languages.append(track.language)

        audio_languages = ", ".join(list(set(audio_languages)))
        subtitle_languages = ", ".join(list(set(subtitle_languages)))

        if codec == "AVC":
            codec = "h264"
        elif codec == "HEVC":
            codec = "h265"

        return (
            bitrate,
            codec,
            dynamic_range,
            resolution,
            audio_languages,
            subtitle_languages,
        )

    @staticmethod
    def get_media_info_file(file: Path):
        return MovieScrapper.parse_media_info(file.absolute().as_posix())

    @staticmethod
    def get_media_info_video_ts(path: Path):
        for file in path.glob("**/*"):
            if file.is_file():
                (
                    bitrate,
                    codec,
                    dynamic_range,
                    resolution,
                    audio_languages,
                    subtitle_languages,
                ) = MovieScrapper.parse_media_info(file.absolute().as_posix())
                if bitrate != -1:
                    return (
                        bitrate,
                        codec,
                        dynamic_range,
                        resolution,
                        audio_languages,
                        subtitle_languages,
                    )
        return None, None, None, None, None, None

    @staticmethod
    def add_movie(object: PathElement) -> Optional[Movie]:
        hashsum = object.hash_sum
        if object.type == PathElement.ElementType.FILE:
            file_object: FileObject = object
            filename = file_object.file.stem
            absolute_path = file_object.absolute_file_path
            size = Path(file_object.absolute_file_path).stat().st_size
        elif object.type == PathElement.ElementType.PATH:
            path_object: PathObject = object
            filename = path_object.path.stem
            absolute_path = path_object.path.absolute().as_posix()
            size = sum(
                f.stat().st_size
                for f in Path(absolute_path).glob("**/*")
                if f.is_file()
            )
        else:
            logging.error("Movie '%s' not supported by this tool.", object)
            return None

        tmdb.API_KEY = "cca7f8ef19ae1664d6511793f17e4bc9"
        search = tmdb.Search()

        title, year = MovieScrapper.get_year_and_title(filename)

        def search_movie():
            if year > 0:
                return search.movie(query=title, year=year)
            else:
                return search.movie(query=title)

        max_retries = 5
        response = None
        for i in range(0, max_retries):
            if i > 0:
                logging.warning(f"Retrying ({i}/{max_retries}) search for {title}...")
            try:
                response = search_movie()
                break
            except ConnectionError as error:
                logging.warning(error)
            time.sleep(i + 1)

        if response is None:
            logging.error(
                f"Max retries reached. {title} will not be added to the database."
            )
            return None

        if response["results"] is not None and len(response["results"]) > 0:
            result = response["results"][0]
            year = int(result["release_date"][:4])
            title = result["title"]
            tmdb_id = result["id"]
        else:
            logging.error(f'"{title}" not found')
            return None

        if object.type == PathElement.ElementType.FILE:
            file_object: FileObject = object
            (
                bitrate,
                _,
                dynamic_range,
                resolution,
                audio_languages,
                subtitle_languages,
            ) = MovieScrapper.get_media_info_file(Path(file_object.absolute_file_path))
            if bitrate == -1:
                logging.warning(
                    f"The media information for {file_object.absolute_file_path}"
                    " could not be extracted"
                )
                return None
        elif object.type == PathElement.ElementType.PATH:
            path_object: PathObject = object
            if path_object.sub_type != PathObject.SubType.VIDEO_TS:
                logging.error(f"PathObject subtype {path_object.sub_type} is unknown")
                return None
            (
                bitrate,
                _,
                dynamic_range,
                resolution,
                audio_languages,
                subtitle_languages,
            ) = MovieScrapper.get_media_info_video_ts(Path(absolute_path))
            if bitrate is None:
                logging.warning(
                    f"The media information for the VIDEO_TS folder of "
                    f"{path_object.path} could not be extraced"
                )
                return None

        logging.debug(msg=f"Add {title} ({year})")
        return Movie(
            title=title,
            year=year,
            size=size,
            hash=hashsum,
            tmdb_id=tmdb_id,
            audio_languages=audio_languages,
            subtitle_languages=subtitle_languages,
            resolution=resolution,
            dynamic_range=dynamic_range,
            bitrate=bitrate,
            sent=False,
        )

    @staticmethod
    def get_year_and_title(title: str):
        current_year: int = datetime.datetime.now().year

        regexes = [
            [r"^.*\((\d*)\).*$", r"^.*(\(\d*\).*)$"],  # Test for year enclosed by ()
            [r"^.*\{(\d*)\}.*$", r"^.*(\{\d*\}.*)$"],  # Test for year enclosed by {}
            [r"^.*\[(\d*)\].*$", r"^.*(\[\d*\].*)$"],  # Test for year enclosed by []
            [
                r"^.*(\d{4})$",
                r"^.*(\d{4})$",
            ],  # Check if the last 4 characters are digits
        ]

        year = -1
        remove = ""
        group_id = 0
        for year_reg, remove_reg in regexes:
            search = re.search(year_reg, title)
            if search:
                candidate_years = []
                group_cnt = 0
                for group in search.groups():
                    group_cnt += 1
                    try:
                        maybe_year = int(group)
                    except ValueError:
                        continue
                    if 0 <= maybe_year <= current_year:
                        candidate_years.append(maybe_year)
                if len(candidate_years) > 0:
                    year = candidate_years[-1]
                    remove = remove_reg
                    group_id = group_cnt
                    break

        if year > 0 and group_id > 0:
            search = re.search(remove, title)
            if search and group_id <= len(search.groups()):
                string_to_remove = search.groups(group_id)[0]
                title = str.replace(title, string_to_remove, "")

        title = title.replace("_", " ").lower().replace("-", " ").strip()
        title = " ".join(title.split())
        return title, year

    @staticmethod
    def compute_hash(object: PathElement) -> FileObject | PathObject | None:
        if object.type == PathElement.ElementType.FILE:
            file_object: FileObject = object
            file_object.hash_sum = Hasher.hashstring_one_file(
                file=file_object.absolute_file_path,
                blocks=1,
            )
            return file_object
        elif object.type == PathElement.ElementType.PATH:
            path_object: PathObject = object
            if path_object.sub_type == PathObject.SubType.VIDEO_TS:
                files = []
                if path_object.path.is_dir():
                    for video_ts in os.listdir(path_object.path.as_posix()):
                        video_ts_path = path_object.path / video_ts
                        if video_ts_path.is_dir():
                            for file in os.listdir(video_ts_path.as_posix()):
                                files.append(path_object.path / video_ts / file)
                if len(files) == 0:
                    logging.error(f"The path {path_object.path} could not be parsed")
                    return None
                path_object.hash_sum = Hasher.hashstring(
                    files=files,
                    blocks=1,
                )
                return path_object
            else:
                logging.warning(
                    f"{path_object.sub_type} as a path type is not supported"
                )
        return None

    async def run(
        self, folder: Path, user: str, password: str, server_address: str, publish: bool
    ):

        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            file_elements = []
            path_elements = set()
            objects = []
            for root, _, filenames in os.walk(folder.absolute().as_posix()):
                for filename in filenames:
                    path = Path(root)
                    file = Path(filename)
                    if path.stem.lower().strip() == "video_ts":
                        path_elements.add(
                            (path.parent.absolute(), PathObject.SubType.VIDEO_TS)
                        )
                    else:
                        absolute_file_path_string = (path / file).absolute().as_posix()
                        file_elements.append((file, absolute_file_path_string))
                        objects.append(
                            (
                                FileObject(
                                    file=file,
                                    absolute_file_path=absolute_file_path_string,
                                ),
                            )
                        )

            for path, sub_type in path_elements:
                objects.append(
                    (
                        PathObject(
                            path=path,
                            sub_type=sub_type,
                        ),
                    )
                )

            results: List[FileObject | PathObject | None] = pool.starmap(
                MovieScrapper.compute_hash, objects
            )

            arguments: List[Tuple[FileObject | PathObject]] = []
            for result in results:
                if result is None:
                    continue
                if len(Movies.select().where(Movies.hash == result.hash_sum)) == 0:
                    arguments.append((result,))

            movies: List[Movie | None] = pool.starmap(
                MovieScrapper.add_movie, arguments
            )

            # For publishing movies
            new_movies: List[Movie] = []
            # For storing them into the database
            new_movies_db: List[Movies] = []

            for movie in movies:
                if movie is None:
                    continue
                new_movies.append(movie)
                new_movies_db.append(
                    Movies.create(
                        title=movie.title,
                        year=movie.year,
                        size=movie.size,
                        hash=movie.hash,
                        tmdb_id=movie.tmdb_id,
                        audio_languages=movie.audio_languages,
                        subtitle_languages=movie.subtitle_languages,
                        resolution=movie.resolution,
                        dynamic_range=movie.dynamic_range,
                        bitrate=movie.bitrate,
                        sent=movie.sent,
                    )
                )
            Movies.insert_many(new_movies_db)
            database.commit()

        logging.info(
            "New movies:\n  %s",
            "\n  ".join(
                [
                    f"{i+1}. {m.title}"
                    for i, m in enumerate(Movies.select().where(Movies.sent == 0))
                ]
            ),
        )

        if not publish:
            logging.info(
                "Publishing was not requested,"
                + " if you want to publish found movies to the server"
                + " make sure to pass '--publish' as a parameter."
            )
            return

        movies_published_successfully = await publish_movies(
            server_address=server_address,
            username=user,
            password=password,
            movies=new_movies,
        )
        Movies.update({Movies.sent: 1 if movies_published_successfully else 0}).where(
            Movies.hash.in_([movie.hash for movie in new_movies])
        )
        database.commit()
