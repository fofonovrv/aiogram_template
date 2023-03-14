from contextlib import suppress
from aiogram.utils import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bot.config import TG_TOKEN, handler_rotation
import logging
from bot.filters import register_all_filters
from bot.handlers import register_all_handlers
from bot.database.models import register_models
from bot.database import get_user_bot

logger = logging.getLogger(__name__)
logger.addHandler(handler_rotation)
logger.setLevel(logging.INFO)

async def __on_start_up(dp: Dispatcher) -> None:
    register_all_filters(dp)
    register_all_handlers(dp)
    register_models()
    get_user_bot() 


def start_bot():
    bot = Bot(token=TG_TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)