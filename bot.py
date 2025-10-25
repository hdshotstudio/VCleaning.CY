# bot.py — minimal clean version (ASCII only)
import asyncio
from aiogram import Router, F, Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from os import getenv

router = Router()

def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(
        KeyboardButton(text="Uslugi"),
        KeyboardButton(text="Moi zapisi"),
        KeyboardButton(text="Podderzhka"),
        KeyboardButton(text="Nastroyki"),
    )
    return kb

WELCOME_MAIN = "Privet, {name}!"
WELCOME_DESC = "Dobro pozhalovat v A.V Cleaning - zdes nachinaetsya chistota."
WELCOME_HINT = "Vyberite nuzhnyj razdel nizhe."

@router.message(F.text.in_(["/start", "start", "nachat", "Start"])) 
async def start_cmd(msg: Message):
    text = f"{WELCOME_MAIN.format(name=msg.from_user.full_name or msg.from_user.first_name)}\n\n{WELCOME_DESC}\n\n{WELCOME_HINT}"
    await msg.answer(text, reply_markup=main_menu(), parse_mode=ParseMode.HTML)

async def run_bot():
    bot = Bot(token=token)
    bot = Bot(token=token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(run_bot())
