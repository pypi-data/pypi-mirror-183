# -*- coding: utf-8 -*-
import os
import sqlite3
import json
from os import walk
from pathlib import Path
import multiprocessing
from multiprocessing import Pool
import requests


from MendiaFileScraper.Hasher import Hasher


class MusicScrapper:

    @staticmethod
    def send(band, album):
        try:
            data = {'type': 'music', 'user': "Lukas", 'band': band, 'album': album}
            data = json.dumps(data).encode('utf-8')
            r = requests.post("http://localhost:80", data=data,
                              headers={'content-type': 'application/json; charset=utf-8'})
            if r.status_code != 200:
                print("Failed")
        except Exception as e:
            print("Failed")

    @staticmethod
    def handle_data(folders, connection: sqlite3.Connection, cursor: sqlite3.Cursor):
        with Pool(processes=multiprocessing.cpu_count()) as pool:
            results = pool.starmap(MusicScrapper.add_album, folders)
            print(results)
            for command in results:
                cursor.execute(command)
            connection.commit()

    @staticmethod
    def supported_file_types():
        return [
            ".mp3",
            ".flac",
            ".ogg",
            ".3gp",
            ".oga",
            ".mogg",
            ".opus",
            ".wav",
            ".wma",
            ".aac",
            ".aax"
        ]

    @staticmethod
    def get_supported_files(path):
        f = []
        for (dirpath, dirnames, filenames) in walk(path):
            f.extend(filenames)
            break
        data_folder = Path(path)
        files = []
        for file in f:
            abs_file_path = data_folder / file
            suffix = Path(abs_file_path).suffix.lower()
            if suffix in MusicScrapper.supported_file_types():
                files.append(abs_file_path)
        return files

    @staticmethod
    def add_album(band, album, path):
        files = MusicScrapper.get_supported_files(path)
        hash = Hasher.hashstring(files=files)
        sql_command = 'INSERT INTO music (artist, album, hash) VALUES ("' + band + '", "' + album + '", "' + hash + '");'
        return sql_command

    @staticmethod
    def exists(band, album, cursor: sqlite3.Cursor):
        sql_command = 'SELECT * FROM music WHERE artist="' + band + '" AND album="' + album + '"';
        cursor.execute(sql_command)
        result = cursor.fetchall()
        return len(result) > 0

    def __init__(self, connection: sqlite3.Connection, cursor: sqlite3.Cursor):
        self.sql_command = """
            CREATE TABLE IF NOT EXISTS music (
            artist VARCHAR(666),
            album VARCHAR(666),
            hash VARCHAR(666),
            PRIMARY KEY(artist, album, hash),
            CONSTRAINT uid UNIQUE(artist, album, hash)
            );"""
        self.connection = connection
        self.cursor = cursor

    def create_table(self):
        self.cursor.execute(self.sql_command)

    def run(self, folder):
        args = []
        cnt = 0
        for interpret in os.listdir(folder):
            if os.path.isdir(folder + "\\" + interpret):
                for album in os.listdir(folder + "\\" + interpret):
                    if os.path.isdir(folder + "\\" + interpret + "\\" + album):
                        path = folder + "\\" + interpret + "\\" + album
                        if not MusicScrapper.exists(interpret, album, cursor=self.cursor):
                            MusicScrapper.send(interpret, album)
                            args.append((interpret, album, path))
                            cnt += 1
                            if cnt > multiprocessing.cpu_count() * 32:
                                MusicScrapper.handle_data(args, connection=self.connection, cursor=self.cursor)
                                args = []
                                cnt = 0

        MusicScrapper.handle_data(args, connection=self.connection, cursor=self.cursor)
