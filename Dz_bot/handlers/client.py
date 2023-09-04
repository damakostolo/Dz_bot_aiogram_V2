from aiogram import types , Dispatcher
from create_bot import dp , bot
from kerbords import kb_client , kb_price


# @dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id ,('Привет! Выбери пункт ниже'), reply_markup=kb_client)
    await message.delete()

# @dp.message_handler(commands=['/Стоимость_работы'])
async def message_price (message: types.Message):
    await bot.send_message(message.from_user.id, ('Выбери вид работы '), reply_markup=kb_price )

# @dp.message_handler(commands=['/Время_выполнения'])
async def message_work_time (message: types.Message):
    await bot.send_message(message.from_user.id, ('Дедлайны назначаете вы , но за скорость вы доплачиваете'))

# @dp.message_handler(commands=['/Заказать'])
async def message_order (message: types.Message):
    await bot.send_message(message.from_user.id, ('Написать мне : '), )

# @dp.message_handler(commands=['/Отзывы'])
async def message_reviews (message: types.Message):
    await bot.send_message(message.from_user.id, ('Чат группа: '))

# @dp.message_handler(commands=['/Другой_вопрос'])
async def message_question (message: types.Message):
    await bot.send_message(message.from_user.id, ('Написать мене : '))

# @dp.message_handler(commands=['/Введение_классрум'])
async def message_classroom (message: types.Message):
    await bot.send_message(message.from_user.id, ('Введение классрума от 4000гр/мес '))

# @dp.message_handler(commands=['/Введение_классрум'])
async def message_other (message: types.Message):
    await bot.send_message(message.from_user.id, ('Любая работа выполняеться от 100 гривен , дальше чам сложнее тем больше беру '))

# @dp.message_handler(commands=['/Введение_классрум'])
async def message_back (message: types.Message):
    await bot.send_message(message.from_user.id, ('Привет! Выбери пункт ниже'), reply_markup=kb_client )

def registe_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_message , commands=['start', 'help'])
    dp.register_message_handler(message_price, commands=['Стоимость_работы'] )
    dp.register_message_handler(message_work_time, commands=['Время_выполнения'])
    dp.register_message_handler(message_order, commands=['Заказать'])
    dp.register_message_handler(message_reviews, commands=['Отзывы'])
    dp.register_message_handler(message_question, commands=['Другой_вопрос'] )
    dp.register_message_handler(message_classroom, commands=['Введение_классрум'])
    dp.register_message_handler(message_other , commands=['Другое']) 
    dp.register_message_handler(message_back , commands=['Back'])
