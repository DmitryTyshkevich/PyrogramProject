from pyrogram import types, Client
from app import fsm, db, AUTH_SESSION
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
    user_id = message.from_user.id
    username = message.text
    if db.get_user(username):
        await message.reply("Этот логин уже занят. Пожалуйста, выбери другой.")
    else:
        name = fsm.data.get("name")
        db.add_user(username, name)
        AUTH_SESSION[user_id] = username
        await message.reply(
            f"{name}, регистрация прошла успешно!", reply_markup=reply_keyboard
        )
        fsm.reset_state(user_id)
        del fsm.data["name"]


async def check_username(message: types.Message) -> None:
    """Функция для проверки логина при авторизации"""
    user_id = message.from_user.id
    username = message.text
    if db.get_user(username):
        AUTH_SESSION[user_id] = username
        fsm.reset_state(user_id)
        await message.reply("Вы успешно авторизовались", reply_markup=reply_keyboard)
    else:
        await message.reply("Неверный логин, попробуйте еще раз:")


async def handle_title(bot: Client, message: types.Message) -> None:
    """Функция для обработки  названия задачи"""
    title = message.text
    fsm.data["title"] = title
    await bot.send_message(message.chat.id, "Теперь введите описание:")
    fsm.set_state(message.from_user.id, "WAITING_DESCRIPTION")


async def write_down_task(bot: Client, message: types.Message) -> None:
    """Функция записывает задачу в бд"""
    if not message.text <= 3:
        title = fsm.data["title"]
        description = message.text
        username = AUTH_SESSION.get(message.from_user.id)
        user_id = db.get_user(username)
        db.add_task(user_id, title, description)
        await bot.send_message(message.chat.id, "Задача добавлена!")
        del fsm.data["title"]
        fsm.reset_state(message.from_user.id)

    else:
        await bot.send_message(
            message.chat.id, "Описание слишком короткое, попробуйте еще раз:"
        )
