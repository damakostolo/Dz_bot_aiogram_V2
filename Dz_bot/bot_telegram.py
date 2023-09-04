from aiogram.utils import executor
from create_bot import dp

async def on_startup(_):
    print('Бот вышел в онлайн')

from handlers import client, admin , other

client.registe_handlers_client(dp)
# admin.registe_handlers_admin(dp)
other.registe_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)