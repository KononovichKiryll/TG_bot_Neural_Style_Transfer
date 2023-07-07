from aiogram import types
from loader import dp
from app_keyboard import kb_NST_menu
from handlers.commands_text import NST_style_img_text
from app_states.states import ImgAcceptState


@dp.message_handler(text=NST_style_img_text)
async def command_start(message: types.Message):
    text = 'Загрузи картинку стиля'
    await ImgAcceptState.style.set()
    await message.answer(text, reply_markup=kb_NST_menu)
