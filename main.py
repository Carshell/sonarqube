import asyncio
import os
import sys  
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE" 

dp = Dispatcher()

def calculate_something(a, b, c):
    result = a + b
    # Forgot to return the result!

@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    # EXISTING MISTAKE: Exposing a secure environment variable to the chat (Security Critical)
    await message.answer(f"Hello! Token: {TOKEN}")
    

    try:
        x = 1 * 0
    except Exception:
        pass

async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
