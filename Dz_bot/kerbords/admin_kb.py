from aiogram.types  import ReplyKeyboardMarkup , KeyboardButton 

btn1 = KeyboardButton ('/Загрузить')
btn2 = KeyboardButton('/Отмена' )


kb_admin = ReplyKeyboardMarkup(resize_keyboard=True , one_time_keyboard= True).add(btn1).add(btn2)

