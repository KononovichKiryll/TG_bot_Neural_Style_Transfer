from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp
from app_keyboard import kb_NN_selector
from handlers.commands_text import start_text


@dp.message_handler(Command(start_text))
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}!\n'
                         #  f'Твой id {message.from_user.id}',
                         'Выбери что ты хочешь сделать\n'
                         'или нажми /help если нужна помощь\n',
                         reply_markup=kb_NN_selector)
