from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from app_states.states import ImgAcceptState
from config.config import CACHE_PATH


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_img(message: types.Message):
    await message.reply('Красивая фотография но я не занаю что с ней делать')


@dp.message_handler(content_types=types.ContentType.PHOTO, state=ImgAcceptState.content)
async def get_content_img(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await message.photo[-1].download(destination_file=f'{CACHE_PATH}/{user_id}/content.jpg')
    await message.reply('Отлично, картинка загружена!')
    await state.finish()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=ImgAcceptState.style)
async def get_style_img(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await message.photo[-1].download(destination_file=f'{CACHE_PATH}/{user_id}/style.jpg')
    await message.reply('Отлично, картинка загружена!')
    await state.finish()
