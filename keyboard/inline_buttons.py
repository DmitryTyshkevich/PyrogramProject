from pyrogram import types


start_button = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                text="Регистрация", callback_data="registration"
            ),
            types.InlineKeyboardButton(
                text="Авторизация", callback_data="authorization"
            ),
        ],
    ]
)
