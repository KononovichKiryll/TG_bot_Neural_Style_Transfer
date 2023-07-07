from aiogram import types
from loader import dp
from app_keyboard import kb_NN_selector
from handlers.commands_text import back_text


@dp.message_handler(text=back_text)
async def command_start(message: types.Message):
    await message.answer('Что-нибудь ещё?',
                         reply_markup=kb_NN_selector)
