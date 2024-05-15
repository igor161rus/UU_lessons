from pony.orm import Database, Required, Json
from settings import DB_CONFIG

db = Database()
db.bind(**DB_CONFIG)


class UserState(db.Entity):
    user_id = Required(str, unique=True)
    scenario_name = Required(str)
    step_name = Required(int)
    context = Required(Json)


class Registration(db.Entity):
    name = Required(str)
    email = Required(str)


db.generate_mapping(create_tables=True)
