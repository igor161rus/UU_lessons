from pony.orm import Database
from settings import DB_CONFIG

db = Database()
db.bind(**DB_CONFIG)

