from aiogram import types
from loader import dp
from app_keyboard import kb_settings
from handlers.commands_text import settings_text, set_resolution_text,set_iterations_text
from app_states.states import ImgAcceptState

from aiogram.dispatcher import FSMContext
from config.config import CACHE_PATH
from utils.NN_settings import change_conf


@dp.message_handler(text=settings_text)
async def command_start(message: types.Message):
    text = 'Тут можно задать настроки для модели'\
        'Разрешение рекомендуется задавать в пределах от 128 до 512'\
        'При увеличении разрешения, время обработки изображения будет увеличиваться'\
        'К сожалению сейчас GPU недоступно и обработка изображений в высоком разрешениии будет занимать много времени'\
        '\n\n Количество итераций'\
        'Количество итераций рекомендуется задавать в пределах от 300 до 1000'\
        'При увеличении Количество итераций, время обработки изображения будет пропорционально увеличиваться'\
        '\n\n Настройки по умолчанию:'\
        '\nРазрешение -128'\
        '\nКоличество итераций -300'\

    # await ImgAcceptState.content.set()
    await message.answer(text, reply_markup=kb_settings)


@dp.message_handler(text=set_resolution_text)
async def command_set_resolution(message: types.Message):
    text = 'Новое значение разрешения'
    await ImgAcceptState.set_resolution.set()
    await message.answer(text, reply_markup=kb_settings)


@dp.message_handler(lambda message: message.text.isdigit(), state=ImgAcceptState.set_resolution)
async def get_resolution_value(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    path = f'{CACHE_PATH}/{user_id}'
    change_conf('imgsize', message.text, path)
    await message.reply('Значение разрешения изменено')
    await state.finish()


@dp.message_handler(text=set_iterations_text)
async def command_set_iter_number(message: types.Message):
    text = 'Новое количества итераций'
    await ImgAcceptState.set_iterations.set()
    await message.answer(text, reply_markup=kb_settings)


@dp.message_handler(lambda message: message.text.isdigit(), state=ImgAcceptState.set_iterations)
async def get_iter_number(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    path = f'{CACHE_PATH}/{user_id}'
    change_conf('iterations', message.text, path)
    await message.reply('Значение количества итераций изменено')
    await state.finish()
