from pyrogram import Client
from decouple import config

from db.d_base import Database
from fsm.custom_fsm import FSM


bot_token = config("BOT_TOKEN")
db_path = config("DB_PATH")

handlers = {"root": "handlers"}

bot = Client("PyApp", bot_token=bot_token, plugins=handlers)
db = Database(db_path)
fsm = FSM()


if __name__ == "__main__":
    bot.run()
