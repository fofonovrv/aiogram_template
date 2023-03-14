from typing import Final
from aiogram.dispatcher.filters.state import StatesGroup, State


class TestState(StatesGroup):
	param1 = State()
	param2 = State()
	param3 = State()