from aiogram import Dispatcher
from aiogram.types import Message
from bot.keyboards import get_main_keyboard
from bot.database.methods.other import get_or_create_user
import logging
from bot.utils.states import TestState
from bot.config import TG_AMINN_ACC
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

logger = logging.getLogger(__name__)
hello_text = 'Привет, дорогой друг!\n'
help_text = '''
/admin - админка
/support - написать админу
/help - помощь
/test_state - тест машины состояний
'''

async def process_start_command(msg: Message):
	user = get_or_create_user(msg)
	await msg.answer(help_text)

async def process_help_command(msg: Message):
	await msg.answer(help_text)

async def process_support_command(msg: Message):
	await msg.answer(f'При возникновении проблем и вопросов вы можете написать создателю бота:\n{TG_AMINN_ACC}')

# test process states
# exit from state
async def cancel_handler(msg: Message, state: FSMContext):
	current_state = await state.get_state()
	if not current_state:
		return
	await state.finish() 
	await msg.answer('Ок')


async def test_state(msg: Message):
	await TestState.param1.set()
	await msg.answer('Активировано состояние TestState.\nВыйти - /cancel')
	await msg.answer('Введи параметр 1 (загрузи фото)')

async def set_param1(msg: Message, state: FSMContext):
	async with state.proxy() as data:
		data['param1'] = msg.photo[0].file_id
	await TestState.next()
	await msg.answer('Теперь введи параметр 2 (описание)')

async def set_param2(msg: Message, state: FSMContext):
	async with state.proxy() as data:
		data['param2'] = msg.text
	await TestState.next()
	await msg.answer('Теперь введи параметр 3 (хештэги)')

async def set_param3(msg: Message, state: FSMContext):
	async with state.proxy() as data:
		data['param3'] = msg.text
	# write date from finished state
	async with state.proxy() as data:
		text = f'Получены данные:\n \
		Параметр 1 (id фото):  {data["param1"]}\n \
		Параметр 2 (описание):  {data["param2"]}\n \
		Параметр 3 (хештэги):  {data["param3"]}\n'
		await msg.answer(text)
	await msg.answer('Выполнен выход из состояние TestState')
	await state.finish()




def register_user_handlers(dp: Dispatcher):
	dp.register_message_handler(process_start_command, commands='start')
	dp.register_message_handler(process_support_command, commands='support')
	dp.register_message_handler(process_help_command, commands='help')

	# register states handlers
	dp.register_message_handler(test_state, commands='test_state', state=None)
	dp.register_message_handler(set_param1, content_types=['photo'], state=TestState.param1)
	dp.register_message_handler(set_param2, state=TestState.param2)
	dp.register_message_handler(set_param3, state=TestState.param3)

	# register cancel handlers
	dp.register_message_handler(cancel_handler, state='*', commands='cancel')
	dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
	
