from pyrogram import Client
from decouple import config


api_id = config("API_ID")
api_hash = config("API_HASH")
bot_token = config("BOT_TOKEN")

handlers = {"root": "handlers"}

bot = Client("PyApp", bot_token=bot_token, plugins=handlers)


bot.run()
