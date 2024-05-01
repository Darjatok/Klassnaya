import asyncio

from aiogram import Bot, Dispatcher
from handlers import include_routers

bot = Bot(token="7028205352:AAEUzZzpdJHlLDoabeQUvCSRIR8u99aREdM")
dp = Dispatcher()


async def main():
    include_routers(dp)
    await dp.start_polling(bot)
 
 
if __name__ == '__main__':
    asyncio.run(main())
