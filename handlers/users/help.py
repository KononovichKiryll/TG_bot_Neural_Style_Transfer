from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Command
from app_states.states import ImgAcceptState
from handlers.commands_text import help_text


@dp.message_handler(Command(help_text), state=[None, ImgAcceptState.in_proces])
async def command_help(message: types.Message):
    await message.answer('Этот бот сделан для реализации алгоритма Neural Style Transfer '
                         'по переносу стиля с одной картинки на другую. Используй клавиатуру '
                         'для общения с ботом. '
                         'Нажми на Настройки для настройки алгоритма. Скорость обработки фото '
                         'зависит от мощности сервера '
                         'Команда /start запускает бота.\n\n'
                         'Телеграмм автора бота: https://t.me/Kononovichkv '
                         )
