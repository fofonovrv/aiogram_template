from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot.database.methods.get import get_user_by_tg_id


def get_admin_inline_keyboard(user_id: int) -> InlineKeyboardMarkup:
	user = get_user_by_tg_id(user_id)
	if not user.is_admin():
		raise Exception()
	kb = InlineKeyboardMarkup(1)
	kb.add(
		InlineKeyboardButton('📊 Посмотреть статистику', callback_data='get_statistics'),
		InlineKeyboardButton('Выполнить что-то ещё', callback_data='get_test'),
	)
	return kb