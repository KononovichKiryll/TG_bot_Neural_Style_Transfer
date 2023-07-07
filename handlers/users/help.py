from aiogram import types
from loader import dp


# def add_help_handler():
#     @dp.message_handler(text='/help')
#     async def get_message(message: types.Message):
#         await message.answer(f'Привет {message.from_user.full_name}!\n'
#                              f'Помощь?'
#                              )

#     print(dp)


@dp.message_handler(text='/help')
async def command_help(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}!\n'
                         f'Помощь?'
                         )

print(dp)
