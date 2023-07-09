from loader import dp

from aiogram import types
from app_states.states import ImgAcceptState


@dp.message_handler(state=[None, ImgAcceptState.in_proces])
async def errors(message: types.Message):
    await message.answer("Я не знаю эту команду")


@dp.message_handler(state=[ImgAcceptState.content, ImgAcceptState.style])
async def img_erros(message: types.Message):
    await message.answer("Я ожидаю картинку а не команду. Нажми кнопку `Назад` для выхода")


@dp.message_handler(state=[ImgAcceptState.set_resolution, ImgAcceptState.set_iterations])
async def settings_erros(message: types.Message):
    await message.answer("Я ожидаю число а не текст. Нажми кнопку `Назад` для выхода")
