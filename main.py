from aiogram import Bot, Dispatcher, F
from environs import Env
import logging, asyncio

from handlers import start_router


env = Env()
env.read_env() 

dp = Dispatcher()


async def main():
    bot = Bot(env.str("TOKEN"))
    dp.include_router(start_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("bot ishda")
    asyncio.run(main())
