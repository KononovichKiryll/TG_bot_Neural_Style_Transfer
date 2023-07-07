from aiogram import types
from loader import dp
from app_keyboard import kb_NST_menu
from handlers.commands_text import NST_cont_img_text


@dp.message_handler(text=NST_cont_img_text)
async def command_start(message: types.Message):
    text = 'Загрузи картинку для изменения'
    await message.answer(text, reply_markup=kb_NST_menu)
