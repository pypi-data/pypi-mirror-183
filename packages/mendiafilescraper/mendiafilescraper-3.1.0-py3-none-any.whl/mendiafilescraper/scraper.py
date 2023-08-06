import json
import logging
from dataclasses import dataclass
from multiprocessing import freeze_support
from pathlib import Path
from typing import List

from dataclasses_json import dataclass_json

from mendiafilescraper.database import database, tables
from mendiafilescraper.movie_scraper import MovieScrapper


@dataclass_json
@dataclass
class Paths:
    movies: List[str]


@dataclass_json
@dataclass
class Config:
    paths: Paths
    user_name: str
    password: str
    server_address: str


class Scraper:
    @staticmethod
    def print_welcome():
        print("Welcome to the setup of the MendiaFileScraper\n")

    @staticmethod
    def print_options():
        print("\n")
        print("Specify user name        (0)")
        print("Specify password         (1)")
        print("Add directory for movies (2)")
        print("Specify the server       (3)")
        print("Show current config      (4)")
        print("Save                     (5)")
        print("Save and Exit            (6)")
        print("Exit                     (7)")

    @staticmethod
    def specify_username(config: Config) -> Config:
        config.user_name = ""
        while len(config.user_name) < 1:
            try:
                config.user_name = input("Specify a user name: ")
            except KeyboardInterrupt:
                return config
        return config

    @staticmethod
    def specify_password(config: Config) -> Config:
        config.password = ""
        while len(config.password) < 1:
            try:
                config.password = input("Specify a password: ")
            except KeyboardInterrupt:
                return config
        return config

    @staticmethod
    def specify_server(config: Config) -> Config:
        while True:
            try:
                server_address = input(
                    "Enter address of the mendia server you'd like to use "
                    "[protocol://hostname:port]: "
                )
                config.server_address = server_address
            except KeyboardInterrupt:
                return config
            break
        return config

    @staticmethod
    def add_path_movies(config: Config, last_path: str) -> Config:
        while True:
            try:
                last_path = input(f"Movies located at [{last_path}]: ")
                path = Path(last_path)
                if path.exists():
                    config.paths.movies.append(path.absolute().as_posix())
                    return config, last_path
                logging.error("Movie location '%s' does not exist.", path)
            except KeyboardInterrupt:
                return config, last_path

    @staticmethod
    def load_config(file: Path) -> Config:
        try:
            with open(file, "r", encoding="utf8") as json_file:
                return Config.from_json(json_file.read())
        except Exception:
            config = Config(
                paths=Paths(movies=[]),
                user_name="",
                password="",
                server_address="",
            )
            logging.error("Failed to read config file, using default: %s", config)
            return config

    @staticmethod
    def write_config(file: Path, config: Config):
        with open(file, "w", encoding="utf8") as outfile:
            outfile.write(json.dumps(config.to_dict()))

    def get_config_path(self) -> Path:
        return Path(self.dir + "config.txt")

    def __init__(self, debug: bool):
        self.debug = debug
        self.home = str(Path.home())
        self.dir = self.home + "/.mendiafilescraper/"
        Path(self.dir).mkdir(parents=True, exist_ok=True)
        logging.basicConfig(filename=self.dir + "log.txt", level=logging.DEBUG)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level=logging.INFO)
        logging.getLogger().addHandler(console_handler)

    async def setup(self):

        self.print_welcome()

        config = self.load_config(self.get_config_path())

        last_path = ""

        try:
            while True:
                self.print_options()
                selected_option = input("Enter a number (0-7): ")
                try:
                    value = int(selected_option)

                    if value == 0:
                        config = self.specify_username(config)
                        continue
                    if value == 1:
                        config = self.specify_password(config)
                        continue
                    if value == 2:
                        config, last_path = self.add_path_movies(config, last_path)
                        continue
                    if value == 3:
                        config = self.specify_server(config)
                        continue
                    if value == 4:
                        logging.info("%s", config)
                        continue
                    if value == 5:
                        self.write_config(self.get_config_path(), config)
                        continue
                    if value == 6:
                        self.write_config(self.get_config_path(), config)
                        return 0
                    if value == 7:
                        return 0

                except ValueError:
                    logging.error("Unknown option")
                    continue
                continue
        except KeyboardInterrupt:
            return 0

    async def scan(self, publish: bool):

        config = self.load_config(self.get_config_path())

        freeze_support()

        database.init(f"{self.dir}database.db")
        database.connect()
        database.create_tables(tables())

        movie_scrapper = MovieScrapper()

        for path in config.paths.movies:
            await movie_scrapper.run(
                Path(path).absolute(),
                user=config.user_name,
                password=config.password,
                server_address=config.server_address,
                publish=publish,
            )

        database.close()
