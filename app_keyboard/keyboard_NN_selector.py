from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from handlers.commands_text import NST_text, settings_text


kb_NN_selector = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=NST_text),
        ],
        [
            KeyboardButton(text=settings_text),
        ],
    ],
    resize_keyboard=True,
)
