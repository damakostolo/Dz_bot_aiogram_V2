from aiogram.types import ReplyKeyboardMarkup , KeyboardButton # , ReplyKeyboardRemove

btn1= KeyboardButton('/Введение_классрум')
btn2= KeyboardButton('/Другое')
btn3= KeyboardButton('/Заказать')

kb_price = ReplyKeyboardMarkup(resize_keyboard=True)

kb_price.add(btn1).add(btn2).add(btn3)