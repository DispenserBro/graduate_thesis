from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage


load_dotenv()
BOT_TOKEN = getenv('TG_TOKEN')

dp = Dispatcher(storage=MemoryStorage())
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.MARKDOWN_V2)

async def main() -> None:
    await dp.start_polling(bot)
