from aiogram import Dispatcher
from aiogram.types import Message
from bot.keyboards import get_main_keyboard
from bot.database import create_msg, get_or_create_user, get_user_bot
import logging

logger = logging.getLogger(__name__)


async def process_text_handler(msg: Message):

	# writing mst to db
	user = get_or_create_user(msg)
	user_bot = get_user_bot()
	create_msg(msg.text, user, user_bot, msg.chat.id)

	await msg.answer('/help - помощь\n/commands - списко команд')


def register_other_handlers(dp: Dispatcher) -> None:
	dp.register_message_handler(process_text_handler, content_types=['text'])