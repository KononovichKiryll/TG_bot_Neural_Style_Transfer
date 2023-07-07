from aiogram.dispatcher.filters import Command

from loader import dp

from aiogram import types
from app_keyboard import kb_test


@dp.message_handler(Command('test'))
async def menu(message: types.Message):
    await message.answer("Hi", reply_markup=kb_test)
