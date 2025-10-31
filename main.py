from aiogram import Bot, Dispatcher, F
import logging, asyncio, os

from dotenv import load_dotenv
from handlers import start_router, user_router



dp = Dispatcher()
load_dotenv()

async def main():
    bot = Bot(os.getenv("TOKEN"))
    dp.include_router(start_router)
    dp.include_router(user_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("bot ishda")
    asyncio.run(main())
