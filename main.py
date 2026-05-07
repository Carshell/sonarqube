import asyncio

import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()



@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("orkerster")



async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
          
