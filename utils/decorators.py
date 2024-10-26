from functools import wraps
from typing import Callable
from pyrogram import Client, types
from app import AUTH_SESSION
from keyboard.inline import start_button


def authorized_only(func: Callable) -> Callable:
    """Декоратор для проверки авторизации"""
    @wraps(func)
    async def wrapper(bot: Client, message: types.Message, *args, **kwargs) -> None:
        user_id = message.from_user.id
        if AUTH_SESSION.get(user_id) is not None:
            return await func(bot, message, *args, **kwargs)
        await bot.send_message(
            message.chat.id,
            "Вы не авторизованы. Пожалуйста, пройдите авторизацию.",
            reply_markup=start_button,
        )

    return wrapper
