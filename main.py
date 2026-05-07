import asyncio
import os
import json  
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

load_dotenv()

TOKEN = "1234567890:ABCdefGhI_JklmnoPqRsTuvWXyz" 

dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:

    useless_variable = "Я просто існую" 
    

    
    return  
    await message.answer("a pon")  


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
