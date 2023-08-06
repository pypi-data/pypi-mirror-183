import asyncio
import datetime
import json
import sys
import time
import multiprocessing
import os
from enum import Enum
import sqlite3
import websockets
from typing import Dict, List
from MendiaFileScraper.PathElement import PathElement, FileObject, PathObject
from pathlib import Path
import tmdbsimple as tmdb
import requests
from MendiaFileScraper.Hasher import Hasher
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from pymediainfo import MediaInfo
import re
import logging


@dataclass_json
@dataclass
class Movie:
    title: str
    year: int
    size: int
    hash: str
    tmdb_id: int
    audio_languages: str
    subtitle_languages: str
    resolution: str
    dynamic_range: str
    bitrate: int
    sent: bool

@dataclass_json
@dataclass
class PushMovies:
    type: str
    username: str
    api_key: str
    movies: List[Movie]

@dataclass_json
@dataclass
class PushMoviesResult:
    success: bool
    reason: str

@dataclass_json
@dataclass
class LoginCredentials:
    type: str
    username: str
    password: str

@dataclass_json
@dataclass
class LoginFailed:
    type: str
    reason: str

@dataclass_json
@dataclass
class Session:
    type: str
    username: str
    api_key: str

class MovieScrapper:

    def __init__(self, connection: sqlite3.Connection, cursor: sqlite3.Cursor):
        self.sql_command = """
            CREATE TABLE IF NOT EXISTS movies (
            title VARCHAR(666),
            year INTEGER,
            size INTEGER,
            hash VARCHAR(666),
            tmdb_id INTEGER,
            audio_languages VARCHAR(666),
            subtitle_languages VARCHAR(666),
            resolution VARCHAR(666),
            dynamic_range VARCHAR(666),
            bitrate INTEGER,
            sent INTEGER,
            PRIMARY KEY(title, year, size, hash),
            CONSTRAINT uid UNIQUE(title, year, size, hash)
            );"""
        self.connection = connection
        self.cursor = cursor

    def create_table(self):
        self.cursor.execute(self.sql_command)

    @staticmethod
    def exists(title: str, year: int, size: int, cursor: sqlite3.Cursor):
        sql_command = f'SELECT * FROM movies WHERE title="{title}" ' \
                      f'AND year="{year}" AND size="{size}";'
        cursor.execute(sql_command)
        result = cursor.fetchall()
        return len(result) > 0

    @staticmethod
    def exists_hash(hash: str, cursor: sqlite3.Cursor):
        sql_command = f'SELECT hash FROM movies WHERE hash="{hash}";'
        cursor.execute(sql_command)
        result = cursor.fetchall()
        return len(result) > 0

    @staticmethod
    def parse_media_info(path: str):

        try:
            media_info = MediaInfo.parse(
                filename=path,
                full=True,
                parse_speed=0.1,
            )
        except FileNotFoundError as e:
            return -1, None, None, None, None, None
            logging.error(str(e))
        except ValueError as e:
            return -1, None, None, None, None, None
            logging.error(str(e))
        except OSError as e:
            logging.error(str(e))
            return -1, None, None, None, None, None
        except RuntimeError as e:
            logging.error(str(e))
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
            if not found_video and track.track_type == 'Video':
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
                    if "hdr10+" in hdat_string_lower or "hdr10plus" in hdat_string_lower:
                        hdr_type = HDRType.HDR10Plus
                    # Must be HDR10 then
                    if hdr_type == HDRType.NONE:
                        hdr_type = HDRType.HDR10

                if hdr_type == HDRType.DOLBY_VISION:
                    dynamic_range = f"HDR / Dolby Vision"
                elif hdr_type == HDRType.HDR10Plus:
                    dynamic_range = f"HDR / HDR10+"
                elif hdr_type == HDRType.DOLBY_VISION:
                    dynamic_range = f"HDR / HDR10"
                else:
                    # Reset back to SDR if the format is none of the three
                    dynamic_range = "SDR"

                if track.bit_rate is not None:
                    bitrate = track.bit_rate
                elif track.bit_rate_mode == "VBR" and track.maximum_bit_rate is not None:
                    bitrate = track.maximum_bit_rate

                if track.format is not None:
                    codec = track.format

                if track.width is not None and track.height is not None:
                    resolution = f"{track.width}x{track.height}"
            elif track.track_type == 'Audio':
                if track.language is None:
                    audio_languages.append("unknown")
                else:
                    audio_languages.append(track.language)
            elif track.track_type == 'Text':
                if track.language is None:
                    subtitle_languages.append("unknown")
                else:
                    subtitle_languages.append(track.language)

        audio_languages = ', '.join(list(set(audio_languages)))
        subtitle_languages = ', '.join(list(set(subtitle_languages)))

        if codec == "AVC":
            codec = "h264"
        elif codec == "HEVC":
            codec = "h265"

        return bitrate, codec, dynamic_range, resolution, audio_languages, subtitle_languages

    @staticmethod
    def get_media_info_file(file: Path):
        return MovieScrapper.parse_media_info(file.absolute().as_posix())

    @staticmethod
    def get_media_info_video_ts(path: Path):
        for file in path.glob('**/*'):
            if file.is_file():
                bitrate, codec, dynamic_range, resolution, audio_languages, subtitle_languages = \
                    MovieScrapper.parse_media_info(file.absolute().as_posix())
                if bitrate != -1:
                    return bitrate, codec, dynamic_range, resolution, audio_languages, subtitle_languages
        return None, None, None, None, None, None

    @staticmethod
    def add_movie(object: PathElement):
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
            size = sum(f.stat().st_size for f in Path(absolute_path).glob('**/*') if f.is_file())
        else:
            logging.warning("Unsupported type")
            return ""

        tmdb.API_KEY = 'cca7f8ef19ae1664d6511793f17e4bc9'
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
            logging.error(f"Max retries reached. {title} will not be added to the database.")
            return ""

        if response['results'] is not None and len(response['results']) > 0:
            result = response['results'][0]
            year = int(result['release_date'][:4])
            title = result['title']
            tmdb_id = result['id']
        else:
            logging.error(f'"{title}" not found')
            return ""

        if object.type == PathElement.ElementType.FILE:
            file_object: FileObject = object
            bitrate, codec, dynamic_range, resolution, audio_languages, subtitle_languages = \
                MovieScrapper.get_media_info_file(Path(file_object.absolute_file_path))
            if bitrate == -1:
                logging.warning(f"The media information for {file_object.absolute_file_path} could not be extracted")
                return ""
        elif object.type == PathElement.ElementType.PATH:
            path_object: PathObject = object
            if path_object.sub_type != PathObject.SubType.VIDEO_TS:
                logging.error(f"PathObject subtype {path_object.sub_type} is unknown")
                return ""
            bitrate, codec, dynamic_range, resolution, audio_languages, subtitle_languages = \
                MovieScrapper.get_media_info_video_ts(Path(absolute_path))
            if bitrate is None:
                logging.warning(f"The media information for the VIDEO_TS folder of "
                                f"{path_object.path} could not be extraced")
                return ""

        logging.debug(msg=f"Add {title} ({year})")
        sql_command = f'INSERT INTO movies (title, year, size, hash, tmdb_id, audio_languages, subtitle_languages, resolution, dynamic_range, bitrate, sent) ' \
                      f'VALUES ("{title}", {year}, {size}, "{hashsum}", {tmdb_id}, "{audio_languages}", "{subtitle_languages}", "{resolution}", "{dynamic_range}", {bitrate}, {0});'

        return sql_command

    @staticmethod
    def get_year_and_title(title: str):
        current_year: int = datetime.datetime.now().year

        regexes = [
            [r'^.*\((\d*)\).*$', r'^.*(\(\d*\).*)$'],  # Test for year enclosed by ()
            [r'^.*\{(\d*)\}.*$', r'^.*(\{\d*\}.*)$'],  # Test for year enclosed by {}
            [r'^.*\[(\d*)\].*$', r'^.*(\[\d*\].*)$'], # Test for year enclosed by []
            [r'^.*(\d{4})$', r'^.*(\d{4})$'],     # Check if the last 4 characters are digits
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
                title = str.replace(title, string_to_remove, '')

        title = title.replace('_', ' ').lower().replace('-', ' ').strip()
        title = ' '.join(title.split())
        return title, year

    @staticmethod
    def get_movies(title, year, cursor):
        sql_command = f'SELECT * FROM movies WHERE title="{title}" ' \
                      f'AND year="{year}";'
        results = cursor.execute(sql_command)

        movies = []

        for result in results:
            title, year, size, hash, tmdb_id, audio_languages, subtitle_languages, resolution, dynamic_range, bitrate, sent = result
            movies.append(Movie(
                title=title,
                year=year,
                size=size,
                hash=hash,
                tmdb_id=tmdb_id,
                audio_languages=audio_languages,
                subtitle_languages=subtitle_languages,
                resolution=resolution,
                dynamic_range=dynamic_range,
                bitrate=bitrate,
                sent=sent,
            ))

        return movies

    @staticmethod
    def get_movies_not_sent(cursor) -> List[Movie]:
        sql_command = f'SELECT * FROM movies WHERE sent=0;'
        results = cursor.execute(sql_command)

        movies: List[Movie] = []

        for result in results:
            title, year, size, hash, tmdb_id, audio_languages, subtitle_languages, resolution, dynamic_range, bitrate, sent = result
            movies.append(Movie(
                title=title,
                year=year,
                size=size,
                hash=hash,
                tmdb_id=tmdb_id,
                audio_languages=audio_languages,
                subtitle_languages=subtitle_languages,
                resolution=resolution,
                dynamic_range=dynamic_range,
                bitrate=bitrate,
                sent=sent,
            ))

        return movies

    @staticmethod
    def set_movie_sent(movie: Movie, cursor):
        sql_command = f'UPDATE movies SET sent=1 WHERE hash="{movie.hash}";'
        cursor.execute(sql_command)
        pass

    @staticmethod
    def compute_hash(object: PathElement):
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
                        video_ts_path = path_object.path/video_ts
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
                logging.warning(f"{path_object.sub_type} as a path type is not supported")
        return None

    async def run(self, folder: Path, user: str, password: str, server_address: str, publish: bool):

        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            file_elements = []
            path_elements = set()
            objects = []
            for root, _, filenames in os.walk(folder.absolute().as_posix()):
                for filename in filenames:
                    path = Path(root)
                    file = Path(filename)
                    if path.stem.lower().strip() == "video_ts":
                        path_elements.add((path.parent.absolute(), PathObject.SubType.VIDEO_TS))
                    else:
                        absolute_file_path_string = (path / file).absolute().as_posix()
                        file_elements.append((file, absolute_file_path_string))
                        objects.append((FileObject(
                            file=file,
                            absolute_file_path=absolute_file_path_string,
                        ),))

            for path, sub_type in path_elements:
                objects.append((PathObject(
                    path=path,
                    sub_type=sub_type,
                ),))

            results = pool.starmap(MovieScrapper.compute_hash, objects)

            arguments = []

            for result in results:
                if not self.exists_hash(hash=result.hash_sum, cursor=self.cursor):
                    arguments.append((result, ))

            commands = pool.starmap(MovieScrapper.add_movie, arguments)

            for command in commands:
                self.cursor.execute(command)
            self.connection.commit()

        new_movies = self.get_movies_not_sent(self.cursor)
        logging.info("%s", '\n'.join([f"{i+1}. {m.title}" for i, m in enumerate(new_movies)]))

        if not publish:
            logging.info(
                "Publishing was not requested,"+
                " if you want to publish found movies to the server"+
                " make sure to pass '--publish' as a parameter."
            )
            return

        push_msg = PushMovies(
            type="PushMovies",
            username=user,
            api_key="",
            movies=new_movies
        )
        logging.info(f"Publishing to {server_address}")
        for movie in push_msg.movies:
            logging.info(f"\t{movie.title}")

        async with websockets.connect(server_address) as websocket:
            await websocket.send(
                LoginCredentials(type="LoginCredentials", username=user, password=password).to_json()
            )
            try:
                message = await asyncio.wait_for(websocket.recv(), timeout=10)
            except TimeoutError:
                logging.exception("Failed to login !")
                sys.exit(1)

            object: Dict = json.loads(message)
            if "type" in object.keys() and object["type"] == "Session":
                session: Session = Session.from_dict(object)
            elif "type" in object.keys() and object["type"] == "LoginFailed":
                failed: LoginFailed = LoginFailed.from_dict(object)
                logging.error("Login failed: %s", failed.reason)
                sys.exit(1)
            else:
                logging.error("Received unexpected message: %s", str(object))
                sys.exit(1)
            push_msg.api_key = session.api_key

            def push_failed(exc=False, msg=""):
                func = logging.exception if exc else logging.error
                func("Failed to push new movies! %s", msg)
                sys.exit(1)

            await websocket.send(push_msg.to_json())
            try:
                message = await asyncio.wait_for(websocket.recv(), timeout=10)
            except TimeoutError:
                push_failed(exc=True)

            object: Dict = json.loads(message)
            if "type" in object.keys() and object["type"] == "PushMoviesResult":
                push_message_result: PushMoviesResult = PushMoviesResult.from_dict(object)
                if not push_message_result.success:
                    push_failed(msg=push_message_result.reason)
            else:
                push_failed()
            logging.info("Pushed movies successfully!")

        for movie in push_msg.movies:
            self.set_movie_sent(movie=movie, cursor=self.cursor)
        self.connection.commit()
