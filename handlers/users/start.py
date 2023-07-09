from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from loader import dp
from app_keyboard import kb_NN_selector
from handlers.commands_text import start_text
from app_states.states import ImgAcceptState
from utils.NN_settings import create_def_config


@dp.message_handler(Command(start_text), state='*')
async def command_start(message: types.Message, state: FSMContext):
    create_def_config(message.from_user.id)
    curr_state = await state.get_state()
    if not curr_state == ImgAcceptState.in_proces.state:
        await state.finish()

    await message.answer(f'Привет {message.from_user.full_name}!\n'
                         #  f'Твой id {message.from_user.id}',
                         'Выбери что ты хочешь сделать\n'
                         'или нажми /help если нужна помощь\n',
                         reply_markup=kb_NN_selector)
