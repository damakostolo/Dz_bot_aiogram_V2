from aiogram.types import ReplyKeyboardMarkup , KeyboardButton # , ReplyKeyboardRemove

btn1= KeyboardButton('/Стоимость_работы')
btn2= KeyboardButton('/Время_выполнения')
btn3= KeyboardButton('/Заказать')
btn4=KeyboardButton('/Отзывы')
btn5=KeyboardButton('/Другой_вопрос')
btn6=KeyboardButton('/Примеры_работ')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(btn1).add(btn6).add(btn2).row(btn3).insert(btn4).insert(btn5)


