from aiogram import types , Dispatcher
from create_bot import dp , bot
from kerbords import kb_client


# @dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id ,('Привет! Выбери пункт ниже'), reply_markup=kb_client)
    await message.delete()

# @dp.message_handler(commands=['/Стоимость_работы'])
async def message_price (message: types.Message):
    await bot.send_message(message.from_user.id, '')

# @dp.message_handler(commands=['/Время_выполнения'])
async def message_work_time (message: types.Message):
    await bot.send_message(message.from_user.id, '')

# @dp.message_handler(commands=['/Заказать'])
async def message_order (message: types.Message):
    await bot.send_message(message.from_user.id, '')

# @dp.message_handler(commands=['/Отзывы'])
async def message_reviews (message: types.Message):
    await bot.send_message(message.from_user.id, '')

# @dp.message_handler(commands=['/Другой_вопрос'])
async def message_question (message: types.Message):
    await bot.send_message(message.from_user.id, '')

def registe_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_message , commands=['start', 'help'])
    dp.register_message_handler(message_price,commands=['/Стоимость_работы'] )
    dp.register_message_handler(message_work_time, commands=['/Время_выполнения'])
    dp.register_message_handler(message_order, commands=['/Заказать'])
    dp.register_message_handler(message_reviews, commands=['/Отзывы'])
    dp.register_message_handler(message_question, commands=['/Другой_вопрос'] )