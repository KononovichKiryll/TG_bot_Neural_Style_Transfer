from aiogram import types
from loader import dp
from app_keyboard import kb_menu


@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}!\n'
                         f'Твой id {message.from_user.id}',
                         reply_markup=kb_menu)

