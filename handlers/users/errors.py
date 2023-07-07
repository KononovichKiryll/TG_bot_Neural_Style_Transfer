from loader import dp

from aiogram import types
# from app_keyboard import kb_NN_selector


@dp.message_handler()
async def menu(message: types.Message):
    await message.answer("Я не знаю эту команду")
