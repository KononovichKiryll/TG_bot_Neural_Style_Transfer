from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Загрузить картинку контента'),
        ],
        [
            KeyboardButton(text='Загрузить картинку стиля'),
        ],
        [
            KeyboardButton(text='Назад'),
            KeyboardButton(text='Далее'),
        ],
    ],
    resize_keyboard=True,
)
