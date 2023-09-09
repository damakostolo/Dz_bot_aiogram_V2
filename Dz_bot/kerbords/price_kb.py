from aiogram.types import ReplyKeyboardMarkup , KeyboardButton # , ReplyKeyboardRemove

btn1= KeyboardButton('/Введение_классрум')
btn2= KeyboardButton('/Другие_работы')
btn3= KeyboardButton('/Заказать')
btn4= KeyboardButton('/Назад')
btn5= KeyboardButton('/Примеры_работ')

kb_price = ReplyKeyboardMarkup(resize_keyboard=True)

kb_price.add(btn1).add(btn5).add(btn2).insert(btn3).insert(btn4)