from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from handlers.commands_text import NST_text


kb_NN_selector = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=NST_text),
        ],
        [
            KeyboardButton(text='что-то ещё'),
        ],
    ],
    resize_keyboard=True,
)
