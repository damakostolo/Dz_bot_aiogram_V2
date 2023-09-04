from aiogram.types import ReplyKeyboardMarkup , KeyboardButton # , ReplyKeyboardRemove

btn1= KeyboardButton('/Стоимость_работы')
btn2= KeyboardButton('/Время_выполнения')
btn3= KeyboardButton('/Заказать')
btn4=KeyboardButton('/Отзывы')
btn5=KeyboardButton('/Другой_вопрос')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(btn1).add(btn2).add(btn3).row(btn4, btn5)


