from pyrogram import Client, filters, types
from keyboard import inline_buttons, main_keyboard


@Client.on_message(filters.command("start"))
async def start(bot: Client, message: types.Message) -> None:
    await bot.send_message(
        message.chat.id,
        "👋 Здравствуйте! Пройдите регистрацию или авторизуйтесь:",
        reply_markup=inline_buttons.start_button,
    )


@Client.on_callback_query(filters.regex("registration"))
async def get_name(bot: Client, call: types.CallbackQuery) -> None:
    bot.answer_callback_query(call.id)
    await call.message.reply("Введите имя:")
