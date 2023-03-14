from aiogram import Dispatcher
from aiogram.dispatcher.filters import Filter
from aiogram.types import Message
from bot.config import TG_ADMIN_ID


class IsAdmin(Filter):
    key = "is_admin"

    async def check(self, message: Message) -> bool:
        return message.from_user.id in TG_ADMIN_ID


# class NotAdmin(Filter):
#     key = "not_admin"

#     async def check(self, message: Message) -> bool:
#         return False if is_admin(message.from_user.id) else True


# class NotVip(Filter):
#     key = "not_vip"

#     async def check(self, message: Message) -> bool:
#         return False if is_vip(message.from_user.id) else True


def register_all_filters(dp: Dispatcher):
    filters = (
        # NotAdmin,
        IsAdmin,
        # NotVip
    )
    for filter in filters:
        dp.bind_filter(filter)