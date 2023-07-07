from loader import dp

from aiogram import types
from app_states.states import ImgAcceptState
# from app_keyboard import kb_NN_selector


@dp.message_handler()
async def errors(message: types.Message):
    await message.answer("Я не знаю эту команду")


@dp.message_handler(state=ImgAcceptState.all_states_names)
async def img_erros(message: types.Message):
    await message.answer("Я ожидаю картинку а не команду")
