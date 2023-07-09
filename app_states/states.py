from aiogram.dispatcher.filters.state import StatesGroup, State


class ImgAcceptState(StatesGroup):
    content = State()
    style = State()
    in_proces = State()
    set_resolution = State()
    set_iterations = State()
