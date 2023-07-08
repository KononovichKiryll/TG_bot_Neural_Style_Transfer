from aiogram import types
from loader import dp,bot
from app_keyboard import kb_NN_selector, kb_NST_menu
from config.config import CACHE_PATH
from handlers.commands_text import next_text
from aiogram.dispatcher import FSMContext
import asyncio


from asyncio import coroutine
# from model.NST_model import run_model
from model.NST_model import ModelRunning

import os

import time

expected_time = 10

# from aiogram.dispatcher import


@dp.message_handler(text=next_text, state='*')
@dp.async_task
async def command_start(message: types.Message, state: FSMContext):
    await state.finish()

    user_id = message.from_user.id
    content_img_path = f'{CACHE_PATH}/{user_id}/content.jpg'
    style_img_path = f'{CACHE_PATH}/{user_id}/style.jpg'
    output_img_path = f'{CACHE_PATH}/{user_id}/output.jpg'

    if not os.path.exists(style_img_path):
        await message.answer('Добавь картинку стиля', reply_markup=kb_NST_menu)
    elif not os.path.exists(content_img_path):
        await message.answer('Добавь картинку контента', reply_markup=kb_NST_menu)
    else:
        await message.answer(f'Начинаю переносить стиль. Это займёт около {expected_time} минут',
                             reply_markup=kb_NN_selector)

        # await dp._loop_create_task(send_img(style_img_path, content_img_path, output_img_path))
        # asyncio.create_task(send_img(message,style_img_path, content_img_path, output_img_path))
        # await send_img(message,style_img_path, content_img_path, output_img_path)

        loop=asyncio.get_running_loop()
        aaaa=ModelRunning(message,style_img_path, content_img_path, output_img_path,loop)
        aaaa.start()
        message.chat.id
        # await aaaa.send()

        # await run_model(style_img_path, content_img_path, output_img_path)
        # print('1111111')
        # with open(output_img_path, 'rb') as output_file:
        #     await message.answer_photo(output_file)
        # with open(output_img_path, 'rb') as output_file:
        #     await message.answer_photo(output_file)
        # await send_img(style_img_path, content_img_path, output_img_path)

        # loop = asyncio.get_event_loop()
        # # Blocking call which returns when the hello_world() coroutine is done
        # loop.run_until_complete(send_img2(message, style_img_path,
        #                         content_img_path, output_img_path))
        # loop.close()
        # await send_img2(message,style_img_path, content_img_path, output_img_path)

        print(asyncio.get_running_loop())

        # await asyncio.to_thread(run_model(style_img_path, content_img_path, output_img_path))
        # run_model(style_img_path, content_img_path, output_img_path)
        # with open(output_img_path, 'rb') as output_file:
        #     await message.answer_photo(output_file)


# @coroutine
# dp.loop
dp._loop_create_task
async def send_img(message, style_img_path, content_img_path, output_img_path):

    # for i in range(10):
    # time.sleep(1)
    # await asyncio.sleep(1)
    # print(i)
    aaaa = ModelRunning(message, style_img_path, content_img_path, output_img_path)
    aaaa.start()

    with open(output_img_path, 'rb') as output_file:
        await message.answer_photo(output_file)

# from aiogram.methods.send_message.SendMessage
# @dp.async_task


@asyncio.coroutine
def send_img2(message, style_img_path, content_img_path, output_img_path):

    for i in range(10):
        time.sleep(1)
        # await asyncio.sleep(1)
        print(i)
    # aaaa=ModelRunning(message,style_img_path, content_img_path, output_img_path)
    # aaaa.start()

    # with open(output_img_path, 'rb') as output_file:
    #     await message.answer_photo(output_file)
