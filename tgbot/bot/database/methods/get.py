from sqlalchemy import exc

from bot.database.main import Database
from bot.database.models import User, Message
from bot.database import create_user


def get_user_by_tg_id(tg_id: int) -> User:
	try:
		return Database().session.query(User).filter(User.tg_id == tg_id).one()
	except exc.NoResultFound:
		return None

def get_all_tg_id() -> list:
	return Database().session.query(User.tg_id).all()

def get_user_count() -> int:
	return Database().session.query(User).count()

def get_msg_count() -> int:
	return Database().session.query(Message).count()