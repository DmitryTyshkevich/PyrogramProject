from pyrogram import Client, filters, types
from filters.custom_filters import reg_filter
from keyboard import inline_buttons
from app import fsm
from utils.func import handle_name, handle_username


@Client.on_message(filters.command("start"))
async def start(bot: Client, message: types.Message) -> None:
    await bot.send_message(
        message.chat.id,
        "👋 Здравствуйте! Пройдите регистрацию или авторизуйтесь:",
        reply_markup=inline_buttons.start_button,
    )


@Client.on_callback_query(reg_filter)
async def enter_name(bot: Client, call: types.CallbackQuery) -> None:
    await bot.answer_callback_query(call.id)
    await call.message.reply("Введите имя:")
    fsm.set_state(call.from_user.id, "WAITING_NAME")


@Client.on_message(filters.text)
async def get_data_users(bot: Client, message: types.Message) -> None:
    state = fsm.get_state(message.from_user.id)
    if state == "WAITING_NAME":
        await handle_name(bot, message)

    elif state == "WAITING_USERNAME" and len(message.text) >= 2:
        await handle_username(message)


@Client.on_message()
async def other(bot: Client, message: types.Message) -> None:
    state = fsm.get_state(message.from_user.id)
    if state == "WAITING_NAME":
        await bot.send_message(message.chat.id, "Нужно ввести имя:")
    elif state == "WAITING_USERNAME":
        await bot.send_message(message.chat.id, "Нужно ввести логин:")
