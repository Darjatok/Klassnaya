from aiogram.fms.state import State, StatesGroup


class Anketa(StatesGroup):
    name = State()
    age = State()
    gender= State()