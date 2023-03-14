import sqlalchemy.exc
import datetime as dt
from bot.database.main import Database
# from bot.database.methods.create import
from bot.database.models import User, Message
from aiogram import types
import logging

logger = logging.getLogger(__name__)

def create_user(msg:types.Message) -> User:
	session = Database().session
	try:
		user = session.query(User.tg_id).filter(User.tg_id == msg.from_user.id).one()
	except sqlalchemy.exc.NoResultFound:
		user = User(
			tg_id=msg.from_user.id,
			username = msg.from_user.username,
			first_name = msg.from_user.first_name,
			last_name = msg.from_user.last_name
			)
		session.add(user)
		session.commit()
		logger.info(f'Создан пользователь: ID={user.tg_id}, {user.username} ({user.first_name} {user.last_name})')
		return user

def create_msg(text:str,from_user:User,to_user:User,chat_id:int):
	session = Database().session
	message = Message(
		from_user=from_user.id,
		to_user=to_user.id,
		chat_id=chat_id,
		text=text, 
		date=dt.datetime.now()
	)
	session.add(message)
	session.commit()
	logger.info(f'From: {from_user.username}, To: {to_user.username}: {text}')