from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Command
from app_states.states import ImgAcceptState
from handlers.commands_text import help_text


@dp.message_handler(Command(help_text), state=[None, ImgAcceptState.in_proces])
async def command_help(message: types.Message):
    text = '''Этот бот сделан для реализации алгоритма Neural Style Transfer по переносу стиля с одной картинки на другую.
Используй клавиатуру для общения с ботом.
Нажми на Настройки для настройки алгоритма.
Скорость обработки фото зависит от мощности сервера

Доступные команды клавиатуры:

- `/start` - запуск бота
- `/help` - помощь
- `Перенос стиля` - переход в меню переноса стиля
     - `Загрузить картинку контента` - загрузка картинки контента
     - `Загрузить картинку стиля` - загрузка картинки контента
     - `Назад` - возврат к предыдущему меню/отмена действия
     - `Далее` - возврат к предыдущему меню/отмена действия
- `Настройки` - переход в меню настроек
     - `Установить разрешение` - установка разрешения для выходной картинки
     - `Установить количество итераций` - установка количества итераций алгоритма
     - `Назад` - возврат к предыдущему меню/отмена действия

Телеграмм автора бота: https://t.me/Kononovichkv '''
    await message.answer(text)
