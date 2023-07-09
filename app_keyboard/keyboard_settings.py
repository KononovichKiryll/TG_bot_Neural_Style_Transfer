from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from handlers.commands_text import back_text, set_iterations_text, set_resolution_text


kb_settings = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=set_resolution_text),
        ],
        [
            KeyboardButton(text=set_iterations_text),
        ],
        [
            KeyboardButton(text=back_text),
        ],
    ],
    resize_keyboard=True,
)
