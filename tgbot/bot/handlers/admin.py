from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from bot.keyboards import get_main_keyboard, get_admin_inline_keyboard
import logging
from bot.database import get_msg_count, get_user_count, get_or_create_user
from aiogram.dispatcher.filters import Text

logger = logging.getLogger(__name__)

	
async def process_admin_command(msg: Message):
	user = get_or_create_user(msg)
	if user.is_admin():
		await msg.answer('<b>Админ панель</b>', reply_markup=get_admin_inline_keyboard(msg.from_user.id))
		# await msg.delete()

async def process_statistic_query(callback: CallbackQuery):
		await callback.message.delete()
		text = f'''
<u>Пользователей:</u>	{get_user_count()}

<u>Текстовых ообщений:</u>	{get_msg_count()}
		'''
		await callback.message.answer(text)
		await callback.answer()

async def proccess_test_query(callback: CallbackQuery):
	await callback.message.delete()
	text = 'Пока действия нет'
	await callback.message.answer(text)
	await callback.answer()
	

def register_admin_handlers(dp: Dispatcher):
	dp.register_message_handler(process_admin_command, commands='admin')
	dp.register_callback_query_handler(process_statistic_query, Text(equals='get_statistics'))
	dp.register_callback_query_handler(proccess_test_query, Text(equals='get_test'))