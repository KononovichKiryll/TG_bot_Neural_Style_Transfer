from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from handlers.commands_text import NST_cont_img_text, NST_style_img_text, back_text, next_text


kb_NST_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=NST_cont_img_text),
        ],
        [
            KeyboardButton(text=NST_style_img_text),
        ],
        [
            KeyboardButton(text=back_text),
            KeyboardButton(text=next_text),
        ],
    ],
    resize_keyboard=True,
)
