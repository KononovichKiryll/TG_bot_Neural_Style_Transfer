import logging

from aiogram import Dispatcher

from config.config import admins_id


async def on_startup_notify(dp: Dispatcher):
    for admin in admins_id:
        try:
            text = 'Bot is started'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)
