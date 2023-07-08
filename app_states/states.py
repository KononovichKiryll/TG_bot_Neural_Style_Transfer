from aiogram.dispatcher.filters.state import StatesGroup, State


class ImgAcceptState(StatesGroup):
    content = State()
    style = State()
    in_proces = State()
