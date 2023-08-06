from typing import List

from peewee import CharField, IntegerField, Model, SqliteDatabase

# Deferred initialization because the sqlite filename is not yet known.
# http://docs.peewee-orm.com/en/latest/peewee/database.html#deferring-initialization
database = SqliteDatabase(None)


class Movies(Model):
    title = CharField(max_length=666)
    year = IntegerField()
    size = IntegerField()
    hash = CharField(max_length=666, primary_key=True, unique=True)
    tmdb_id = IntegerField()
    audio_languages = CharField(max_length=666)
    subtitle_languages = CharField(max_length=666)
    resolution = CharField(max_length=666)
    dynamic_range = CharField(max_length=666)
    bitrate = IntegerField()
    sent = IntegerField()

    class Meta:
        database = database


def tables() -> List[Model]:
    return [Movies]
