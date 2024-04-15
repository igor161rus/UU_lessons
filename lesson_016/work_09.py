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

new_artist = Artist(name='Led Zeppelin')
new_artist.save()
# new_album = Album.create(artist=new_artist, title='Led Zeppelin IV',
#                          release_date=datetime.datetime(1971, 11, 1),
#                          publisher='Atlantic', media_type='LP')

albums = [
    {
        'artist': 'Led Zeppelin',
        'title': 'Led Zeppelin III',
        'release_date': datetime.datetime(1970, 10, 22),
        'publisher': 'Atlantic',
        'media_type': 'LP'
    },
    {
        'artist': 'Led Zeppelin',
        'title': 'Led Zeppelin II',
        'release_date': datetime.datetime(1969, 11, 8),
        'publisher': 'Atlantic',
        'media_type': 'LP'
    },
    {
        'artist': 'Led Zeppelin',
        'title': 'Led Zeppelin I',
        'release_date': datetime.datetime(1968, 10, 22),
        'publisher': 'Atlantic',
        'media_type': 'LP'
    }
]

albums_in_db = Album.insert_many(albums).execute()

bands = ['Led Zeppelin', 'Pink Floyd', 'Rolling Stones']
for band in bands:
    Artist.create(name=band)

