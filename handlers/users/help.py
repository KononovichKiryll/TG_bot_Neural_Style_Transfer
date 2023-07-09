from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Command
from app_states.states import ImgAcceptState
from handlers.commands_text import help_text


@dp.message_handler(Command(help_text), state=[None, ImgAcceptState.in_proces])
async def command_help(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}!\n'
                         f'Помощь?'
                         )
