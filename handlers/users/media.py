from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from app_states.states import ImgAcceptState


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_img(message: types.Message):
    # photo_id=message.photo[-1].file_id
    await message.reply('Красивая фотография но я не занаю ято с ней делать')


@dp.message_handler(content_types=types.ContentType.PHOTO, state=ImgAcceptState.content)
async def get_content_img(message: types.Message, state: FSMContext):
    # photo_id=message.photo[-1].file_id
    await message.reply('Это картинка контента')
    await state.finish()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=ImgAcceptState.style)
async def get_style_img(message: types.Message, state: FSMContext):
    # photo_id=message.photo[-1].file_id
    await message.reply('Это картинка стиля')
    await state.finish()
