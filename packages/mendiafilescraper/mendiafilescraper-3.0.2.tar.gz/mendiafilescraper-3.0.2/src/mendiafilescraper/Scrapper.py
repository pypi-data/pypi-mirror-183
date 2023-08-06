# -*- coding: utf-8 -*-
import logging
import sqlite3
import json
from json import JSONDecodeError
from multiprocessing import freeze_support
from pathlib import Path
import sys
from mendiafilescraper.MusicScrapper import MusicScrapper
from mendiafilescraper.MovieScrapper import MovieScrapper


class Scrapper:

    @staticmethod
    def print_welcome():
        print("Welcome to the setup of the MendiaFileScraper\n")

    @staticmethod
    def print_options():
        print("\n")
        print("Specify user name        (0)")
        print("Specify password         (1)")
        print("Add directory for music  (2)")
        print("Add directory for movies (3)")
        print("Specify the server       (4)")
        print("Show current config      (5)")
        print("Save                     (6)")
        print("Save and Exit            (7)")
        print("Exit                     (8)")

    @staticmethod
    def specify_username(data):
        data['user_name'] = ""
        while len(data['user_name']) < 1:
            try:
                data['user_name'] = input("Specify a user name: ")
            except KeyboardInterrupt:
                return
        return data

    @staticmethod
    def specify_password(data):
        data['password'] = ""
        while len(data['password']) < 1:
            try:
                data['password'] = input("Specify a password: ")
            except KeyboardInterrupt:
                return
        return data

    @staticmethod
    def specify_server(data):
        while True:
            try:
                server_address = input("Enter address of the mendia server you'd like to use [protocol://hostname:port]: ")
                data['server_address'] = server_address
            except KeyboardInterrupt as e:
                logging.error(msg=f"KeyboardInterrupt: {e.msg}")
                return
            break
        return data

    @staticmethod
    def add_path_music(data, last_path):
        while True:
            try:
                last_path = input(f"Music located at [{last_path}]: ")
                path = Path(last_path)
                if path.exists():
                    data['paths']['music'].append(path.absolute().as_posix())
                    return data, last_path
                else:
                    logging.error(msg=f"Music path does not exist: {str(path)}")
            except KeyboardInterrupt as e:
                logging.error(msg=f"KeyboardInterrupt: {e.msg}")
                return data, last_path

    @staticmethod
    def add_path_movies(data, last_path):
        while True:
            try:
                last_path = input(f"Movies located at [{last_path}]: ")
                path = Path(last_path)
                if path.exists():
                    data['paths']['movies'].append(path.absolute().as_posix())
                    return data, last_path
                else:
                    print("Path does not exist")
            except KeyboardInterrupt as e:
                logging.error(msg=f"KeyboardInterrupt: {e.msg}")
                return data, last_path

    @staticmethod
    def load_config(file):
        filename = Path(file)
        filename.touch(exist_ok=True)
        with open(file, 'r') as json_file:
            try:
                return json.load(json_file)
            except JSONDecodeError as e:
                logging.error(msg=f"JSONDecodeError: {e.msg}")
                return {}

    @staticmethod
    def write_config(file, data):
        with open(file, 'w') as outfile:
            json.dump(data, outfile)

    def get_config_path(self):
        return self.dir+'config.txt'

    def __init__(self, debug: bool):
        self.debug = debug
        self.home = str(Path.home())
        self.dir = self.home + "/.mendiamilescraper/"
        Path(self.dir).mkdir(parents=True, exist_ok=True)
        logging.basicConfig(filename=self.dir+"log.txt", level=logging.DEBUG)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level=logging.INFO)
        logging.getLogger().addHandler(console_handler)

    def setup(self):

        data = self.load_config(self.get_config_path())

        self.print_welcome()

        if 'paths' not in data:
            data['paths'] = {}

        if 'movies' not in data['paths']:
            data['paths']['movies'] = []

        if 'music' not in data['paths']:
            data['paths']['music'] = []

        last_path = ""

        try:
            while True:
                self.print_options()
                selected_option = input("Enter a number (0-8): ")
                try:
                    value = int(selected_option)

                    if value == 0:
                        data = self.specify_username(data)
                        continue
                    elif value == 1:
                        data = self.specify_password(data)
                        continue
                    elif value == 2:
                        data, last_path = self.add_path_music(data, last_path)
                        continue
                    elif value == 3:
                        data, last_path = self.add_path_movies(data, last_path)
                        continue
                    elif value == 4:
                        data = self.specify_server(data)
                        continue
                    elif value == 5:
                        logging.info(data)
                        continue
                    elif value == 6:
                        self.write_config(self.get_config_path(), data)
                        continue
                    elif value == 7:
                        self.write_config(self.get_config_path(), data)
                        return
                    elif value == 8:
                        return

                except ValueError:
                    print("Unknown option")
                    continue
                print("Unknown option")
                continue
        except KeyboardInterrupt:
            sys.exit(0)

    async def scan(self, publish: bool):

        data = self.load_config(self.get_config_path())

        if 'user_name' not in data:
            print("User name is missing")
            return

        if 'password' not in data:
            print("Password is missing")
            return

        if 'server_address' not in data:
            print("Address to the mendia server is missing")
            return

        freeze_support()
        connection = sqlite3.connect(self.dir+"database.db")
        cursor = connection.cursor()

        music_scrapper = MusicScrapper(connection=connection, cursor=cursor)
        music_scrapper.create_table()

        if 'paths' in data:
            if 'music' in data['paths']:
                for path in data['paths']['music']:
                    # music_scrapper.run(Path(path).absolute())
                    continue

        movie_scrapper = MovieScrapper(connection=connection, cursor=cursor)
        movie_scrapper.create_table()

        if 'paths' in data:
            if 'music' in data['paths']:
                for path in data['paths']['movies']:
                    await movie_scrapper.run(
                        Path(path).absolute(),
                        user=data['user_name'],
                        password=data['password'],
                        server_address=data['server_address'],
                        publish=publish,
                    )

        connection.commit()
        connection.close()
