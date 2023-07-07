from aiogram.dispatcher.filters.state import StatesGroup, State


class ImgAcceptState(StatesGroup):
    default = State()
    content = State()
    style = State()
