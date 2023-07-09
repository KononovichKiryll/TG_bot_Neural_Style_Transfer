from aiogram import types
from loader import dp
from app_keyboard import kb_NST_menu
from handlers.commands_text import NST_text, settings_text
from app_states.states import ImgAcceptState


@dp.message_handler(text=NST_text)
async def command_NST_menu(message: types.Message):
    text = 'Я сделаю перенос стиля на картинку по алгоритму NST.\n'\
        'Выбери картинку которую хочешь поментять\n'\
        'и картинку с которой нужно взять стиль.\n'\
        'Затем нажми далее и я начну.\n'

    await message.answer(text, reply_markup=kb_NST_menu)


@dp.message_handler(text=[NST_text, settings_text], state=ImgAcceptState.in_proces)
async def command_NST_menu_in_process(message: types.Message):
    text = 'Пока что я занимаюсь предыдущей задачей, но я скоро закончу!\n'

    await message.answer(text)
