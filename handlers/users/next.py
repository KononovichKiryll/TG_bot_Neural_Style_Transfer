from aiogram import types
from loader import dp
from app_keyboard import kb_NN_selector, kb_NST_menu

from handlers.commands_text import next_text

expected_time = 10


@dp.message_handler(text=[next_text, '1', '2'])
async def command_start(message: types.Message):
    if message.text == '1':
        await message.answer('Добавь картинку стиля', reply_markup=kb_NST_menu)
    elif message.text == '2':
        await message.answer('Добавь картинку контента', reply_markup=kb_NST_menu)
    else:
        await message.answer(f'Начинаю переносить стиль. Это займёт около {expected_time} минут',
                             reply_markup=kb_NN_selector)
