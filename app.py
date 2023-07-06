from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
from dotenv import dotenv_values

load_dotenv()
TOKEN = dotenv_values()['TOKEN']

bot = Bot(token=TOKEN)

dp = Dispatcher(bot=bot)


@dp.message_handler()
# async def get_message(message):
async def get_message(message: types.Message):
    chat_id = message
    print(message)

    chat_id = message.chat.id
    text = 'hhhhi'

    await bot.send_message(chat_id=chat_id, text=text)
    
    await message.answer(text)

executor.start_polling(dp)