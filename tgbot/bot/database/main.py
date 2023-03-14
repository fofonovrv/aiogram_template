from typing import Final
from bot.config import DB_STRING
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class SingletonMeta(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        cls._instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance

class Singleton(metaclass=SingletonMeta):
    """Easy use of SingletonMeta"""

class Database(metaclass=SingletonMeta):
	BASE: Final = declarative_base()
	def __init__(self):
		self.__engine = create_engine(DB_STRING)
		session = sessionmaker(bind=self.__engine)
		self.__session = session()
	@property
	def session(self):
		return self.__session
	@property
	def engine(self):
		return self.__engine