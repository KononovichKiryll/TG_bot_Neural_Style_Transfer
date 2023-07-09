from aiogram import types
from aiogram.dispatcher import FSMContext
from app_states.states import ImgAcceptState
from loader import dp
from app_keyboard import kb_NN_selector, kb_NST_menu, kb_settings
from handlers.commands_text import back_text


@dp.message_handler(text=back_text)
async def command_back(message: types.Message):
    await message.answer('Что-нибудь ещё?',
                         reply_markup=kb_NN_selector)


@dp.message_handler(text=back_text, state=[ImgAcceptState.content, ImgAcceptState.style])
async def command_img_back(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Возвращайся если захочешь загрузить картинку',
                         reply_markup=kb_NST_menu)


@dp.message_handler(text=back_text, state=[ImgAcceptState.set_iterations,
                                           ImgAcceptState.set_resolution])
async def command_settings_back(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Настройки не были изменены',
                         reply_markup=kb_settings)
