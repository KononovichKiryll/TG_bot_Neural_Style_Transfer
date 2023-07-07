from aiogram import types
from loader import dp
from app_keyboard import kb_NST_menu
from handlers.commands_text import NST_text


@dp.message_handler(text=NST_text)
async def command_start(message: types.Message):
    text = 'Я сделаю перенос стиля на картинку по алгоритму NST.\n'\
        'Выбери картинку которую хочешь поментять\n'\
        'и картинку с которой нужно взять стиль.\n'\
        'Затем нажми далее и я начну.\n'

    await message.answer(text, reply_markup=kb_NST_menu)
