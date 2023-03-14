from bot.database.models import User
from bot.database.main import Database
from bot.database.methods.get import get_user_by_tg_id
from bot.database.methods.create import create_user
from aiogram.types import Message
from sqlalchemy import exc
import logging

logger = logging.getLogger(__name__)


def get_or_create_user(msg_from_user:Message) -> User:
	user = get_user_by_tg_id(tg_id=msg_from_user.from_user.id)
	if user:
		return user
	else:
		user = create_user(msg_from_user)
		return user

def get_user_bot() -> User:
	session = Database().session
	user_bot = session.query(User).filter(User.tg_id==0).scalar()
	if not user_bot:
		user_bot = User(
			tg_id=0,
			username = 'bot',
			first_name = 'Your',
			last_name = 'Bot'
			)
		session.add(user_bot)
		session.commit()
		logger.info(f'Создан пользователь: ID={user_bot.tg_id}, {user_bot.username} ({user_bot.first_name} {user_bot.last_name})')
	return user_bot