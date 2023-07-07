from aiogram import types, Dispatcher
from handlers.commands_text import help_text, start_text


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand(start_text, 'Запустить бота'),
        types.BotCommand(help_text, 'Помощь'),
        # types.BotCommand('is_this_test', 'test???'),
    ])
