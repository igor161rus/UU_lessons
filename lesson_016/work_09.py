import peewee
import datetime

db = peewee.SqliteDatabase('data/music.db')


class BaseTable(peewee.Model):
    class Meta:
        database = db


class Artist(BaseTable):
    name = peewee.CharField()


class Album(BaseTable):
    artist = peewee.ForeignKeyField(Artist)
    title = peewee.CharField()
    release_date = peewee.DateTimeField()
    publisher = peewee.CharField()
    media_type = peewee.CharField()


db.create_tables([Artist, Album])
