from aiogram import types , Dispatcher
from create_bot import dp 
import json
import string

#  Общая часть

# @dp.message_handler()

async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('cenz.json')))):
        await message.reply('No mat')
        await message.delete()
    else :
        await message.reply('Нет такой команды напишите /help ')
        await message.delete()

def registe_handlers_other (dp: Dispatcher):
    dp.register_message_handler(echo_send)