import asyncio
from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
from handlers import main_handlers, for_menu, says_handler, sovets
import logging
load_dotenv()


async def main():
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(main_handlers.router, for_menu.router, says_handler.router, sovets.router)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
