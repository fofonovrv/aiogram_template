from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from bot.config import TG_ADMIN_ID

from .main import Database


class User(Database.BASE):
	__tablename__ = 'USER'
	id = Column(Integer, primary_key=True)
	tg_id = Column(Integer, comment='ID TG')
	username = Column(String(128), comment='username')
	first_name = Column(String(128), comment='Имя')
	last_name = Column(String(128), comment='Фамилия')
	messages_from = relationship('Message', backref='messages_from_user', lazy='dynamic', foreign_keys='[Message.from_user]')
	messages_to = relationship('Message', backref='messages_to_user', lazy='dynamic', foreign_keys='[Message.to_user]')
	
	def __repr__(self):
		return f'{self.username} ({self.first_name} {self.last_name})'
	
	def is_admin(self) -> bool:
		return str(self.tg_id) in TG_ADMIN_ID


class Message(Database.BASE):
	__tablename__ = 'MESSAGE'
	id = Column(Integer, primary_key=True)
	from_user = Column(Integer, ForeignKey('USER.id'), comment='Отправитель')
	to_user = Column(Integer, ForeignKey('USER.id'), comment='Получатель')
	chat_id = Column(Integer, comment='ID чата')
	text = Column(Text, comment='Текст сообщения')
	date = Column(DateTime, comment='Время и дата')
	def __repr__(self):
		return f'{self.date}: from {self.from_user} to {self.to_user} '


def register_models():
	Database.BASE.metadata.create_all(Database().engine)