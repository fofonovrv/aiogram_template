from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from bot.database.methods.get import get_user_by_tg_id
from copy import deepcopy

def _default_main_menu() -> ReplyKeyboardMarkup:
	btns = (
		KeyboardButton('/menu'),
		KeyboardButton('/support'),
		KeyboardButton('/help'),
	)
	menu = ReplyKeyboardMarkup(resize_keyboard=True)
	for btn in btns:
		menu.add(btn)
	return menu

def _admin_main_menu() -> ReplyKeyboardMarkup:
	btns = (
		KeyboardButton('/menu'),
		KeyboardButton('/statistic'),
		KeyboardButton('/admin'),
	)
	menu = ReplyKeyboardMarkup(resize_keyboard=True)
	for btn in btns:
		menu.add(btn)
	return menu

def get_main_keyboard(tg_id: int) -> ReplyKeyboardMarkup:
	user = get_user_by_tg_id(tg_id)
	if user.is_admin:
		return _admin_main_menu()
	else:
		return _default_main_menu()
		

