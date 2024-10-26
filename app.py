from pyrogram import Client
from decouple import config

from db.d_base import Database
from fsm.custom_fsm import FSM


db_path = config("DB_PATH")

AUTH_SESSION = {}

handlers = {"root": "handlers"}

bot = Client("PyApp", plugins=handlers)
db = Database(db_path)
fsm = FSM()


if __name__ == "__main__":
    bot.run()
