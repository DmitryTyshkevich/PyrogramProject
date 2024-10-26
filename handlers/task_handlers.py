from pyrogram import Client, types, filters
from filters.custom_filters import for_create_task
from utils.decorators import authorized_only
from utils.func import handle_title, write_down_task
from app import fsm


@Client.on_message(for_create_task("Создать задачу"))
@authorized_only
async def create_task(bot: Client, message: types.Message) -> None:
    await bot.send_message(message.chat.id, "Введите название задачи:")
    fsm.set_state(message.from_user.id, "WAITING_TITLE")


@Client.on_message(filters.text)
async def get_data(bot: Client, message: types.Message) -> None:
    state = fsm.get_state(message.from_user.id)
    if state == "WAITING_TITLE":
        await handle_title(bot, message)
    elif state == "WAITING_DESCRIPTION":
        await write_down_task(bot, message)
