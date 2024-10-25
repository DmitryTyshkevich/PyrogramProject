from pyrogram import types, Client
from app import fsm, db
from keyboard.reply import reply_keyboard


async def handle_name(bot: Client, message: types.Message) -> None:
    """Функция для обработки имени при регистрации"""
    if message.text.isalpha() and 2 <= len(message.text) <= 30:
        name = message.text.title()
        fsm.data["name"] = name
        await bot.send_message(message.chat.id, "Теперь введите логин:")
        fsm.set_state(message.from_user.id, "WAITING_USERNAME")
    else:
        await bot.send_message(message.chat.id, "Введите имя:")


async def handle_username(message: types.Message) -> None:
    """Функция для обработки логина при регистрации"""
    username = message.text
    if db.get_user(username):
        await message.reply("Этот логин уже занят. Пожалуйста, выбери другой.")
    else:
        name = fsm.data.get("name")
        db.add_user(username, name)
        await message.reply(
            f"{name}, регистрация прошла успешно!", reply_markup=reply_keyboard
        )
        fsm.reset_state(message.from_user.id)
        del fsm.data["name"]


async def check_username(message: types.Message) -> None:
    """Функция для проверки логина при авторизации"""
    username = message.text
    if db.get_user(username):
        fsm.reset_state(message.from_user.id)
        await message.reply("Вы успешно авторизовались", reply_markup=reply_keyboard)
    else:
        await message.reply("Неверный логин, попробуйте еще раз:")
