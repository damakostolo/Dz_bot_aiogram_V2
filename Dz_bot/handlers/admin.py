from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types , Dispatcher
from create_bot import dp , bot
from aiogram.dispatcher.filters import Text
from data_base import sqli_bd
from kerbords import admin_kb
from aiogram.types import InlineKeyboardButton , InlineKeyboardMarkup


ID = None
 
class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


#Получаем АйДи пользывателя 
# @dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_admin_comands(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id , 'Привет красавчик что надо? ' , reply_markup= admin_kb.kb_admin) 
    await message.delete()


# Начало диалога 

# @dp.message_handler(comands="Загрузить", state= None)
async def cm_start(message: types.Message):
    if ID == message.from_user.id :
        await FSMAdmin.photo.set()
        await message.reply('Отправте фото')
    elif ID != message.from_user.id :
        await message.reply('Только админам')
    # Ловим ответ и записуем 

# @dp.message_handler(content_types=["photo"], state= FSMAdmin.photo)
async def load_photo(message: types.Message, state : FSMContext):
    if ID == message.from_user.id :
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Введите название')

# Выход из состояния 

# @dp.message_handler(state='*', commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ok')

    # Ловим ответ и записуем 

# @dp.message_handler(state= FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if ID == message.from_user.id :
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Введите описание')

    # Ловим ответ и записуем 

# @dp.message_handler(state= FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if ID == message.from_user.id :
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Введите цену')


    # Ловим ответ и записуем 

# @dp.message_handler(state= FSMAdmin.price)
async def load_price(message: types.Message, state : FSMContext):
    if ID == message.from_user.id :
        async with state.proxy() as data:
            data['price'] = float(message.text)
        
        await sqli_bd.sql_add_command(state)
        await state.finish()
        await message.reply('готово')

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqli_bd.sql_delete_command(callback_query.data.replace('del ' , ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")}удалена.', show_alert=True)

@dp.message_handler(commands='Удалить')
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqli_bd.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                   add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))


#регестрируем хендлеры
def registe_handlers_admin(dp:Dispatcher): 
    dp.register_message_handler(cm_start, commands=['Загрузить'], state= None )
    dp.register_message_handler(cancel_handler , Text(equals='отмена', ignore_case=True), state='*' )
    dp.register_message_handler(load_photo , content_types=["photo"], state= FSMAdmin.photo)
    dp.register_message_handler(load_name, state= FSMAdmin.name)
    dp.register_message_handler(load_description,state= FSMAdmin.description )
    dp.register_message_handler(load_price ,state= FSMAdmin.price )
    dp.register_message_handler(cancel_handler , state='*', commands='отмена')
    dp.register_message_handler(make_admin_comands , commands=['moderator'], is_chat_admin=True)