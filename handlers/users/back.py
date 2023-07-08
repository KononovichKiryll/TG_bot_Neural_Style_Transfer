from aiogram import types
from aiogram.dispatcher import FSMContext
from app_states.states import ImgAcceptState
from loader import dp
from app_keyboard import kb_NN_selector, kb_NST_menu
from handlers.commands_text import back_text


@dp.message_handler(text=back_text)
async def command_back(message: types.Message):
    await message.answer('Что-нибудь ещё?',
                         reply_markup=kb_NN_selector)


@dp.message_handler(text=back_text, state=ImgAcceptState.all_states_names)
async def command_img_back(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Возвращайся если захочешь загрузить картинку',
                         reply_markup=kb_NST_menu)
