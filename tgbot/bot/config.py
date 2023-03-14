import os
import logging
from logging.handlers import RotatingFileHandler

TG_TOKEN = os.environ.get('TG_TOKEN', '')

# vars for postgresql
# DB_USER = os.environ.get('POSTGRES_USER')
# DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
# DB_HOST = 'db'
# DB_PORT = '5432'
# DB_NAME = os.environ.get('POSTGRES_DB')
# DB_STRING = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

DB_STRING = 'sqlite:///db.sqlite3'
TG_ADMIN_ID = ['11111']
TG_AMINN_ACC = '@example'

# logging
LOG_GILE = logging.FileHandler('logs/info.log')
LOG_CONSOLE = logging.StreamHandler()

handler_rotation = RotatingFileHandler('logs/info.log', mode='a',maxBytes=1000, backupCount=5)
logging.basicConfig(handlers=(LOG_GILE, LOG_CONSOLE), 
	format='[%(asctime)s | %(levelname)s]: %(message)s', 
	datefmt='%d.%m.%Y %H:%M:%S',
	level=logging.INFO)
