from aiogram import types , Dispatcher
from create_bot import dp , bot


dp.message_handler(commands=['start', 'help'] )
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id ,('Привет! Выбери пункт ниже'))
    await message.delete()


def registe_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_message , commands=['start', 'help'])