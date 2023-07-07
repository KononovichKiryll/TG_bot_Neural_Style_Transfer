from aiogram import types
from loader import dp
from app_keyboard import kb_NN_selector, kb_NST_menu
from config.config import CACHE_PATH
from handlers.commands_text import next_text
from aiogram.dispatcher import FSMContext

import os


expected_time = 10


@dp.message_handler(text=next_text, state='*')
async def command_start(message: types.Message, state: FSMContext):
    await state.finish()

    user_id = message.from_user.id
    content_img_path = f'{CACHE_PATH}/{user_id}/content.jpg'
    style_img_path = f'{CACHE_PATH}/{user_id}/style.jpg'

    if not os.path.exists(style_img_path):
        await message.answer('Добавь картинку стиля', reply_markup=kb_NST_menu)
    elif not os.path.exists(content_img_path):
        await message.answer('Добавь картинку контента', reply_markup=kb_NST_menu)
    else:
        await message.answer(f'Начинаю переносить стиль. Это займёт около {expected_time} минут',
                             reply_markup=kb_NN_selector)
