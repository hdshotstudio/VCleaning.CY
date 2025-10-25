# bot.py — A.V Cleaning (aiogram v3)
import asyncio
from aiogram import Router, F, Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

router = Router()

# Главное меню — в стиле CinCin

def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(
        KeyboardButton(text="🧹 Услуги"),
        KeyboardButton(text="📅 Мои записи"),
        KeyboardButton(text="💬 Поддержка"),
        KeyboardButton(text="⚙️ Настройки"),
    )
    return kb
    
WELCOME = {
    "main": "<b>Привет, {name}!</b>",
    "desc": "Добро пожаловать в <b>A.V Cleaning</b> — здесь чистота начинается с заботы 🧼✨",
    "hint": "Выберите нужный раздел ниже 👇"
}

LOADING_ANIM = ["Загрузка 🧺", "Загрузка 🧼", "Почти готово ✨", "Готово 💎"]

async def show_loading(msg: Message):
    for step in LOADING_ANIM:
        try:
            await msg.edit_text(step)
        except Exception:
            # если сообщение без edit — просто отправим новое
            await msg.answer(step)
        await asyncio.sleep(0.6)

@router.message(F.text.in_(["/start", "start", "начать", "Start", "Старт"]))
async def start_cmd(msg: Message):
    await msg.answer(
        WELCOME.format(name=msg.from_user.full_name or msg.from_user.first_name),
        reply_markup=main_menu(),
        parse_mode=ParseMode.HTML,
    )

@router.message(F.text == "🧹 Услуги")
async def show_services(msg: Message):
    sent = await msg.answer("🕓 Загружаю список услуг…")
    await show_loading(sent)
    await msg.answer("🧹 <b>Выберите услугу</b>
Каждая уборка — с вниманием к деталям ✨", parse_mode=ParseMode.HTML)

@router.message(F.text == "📅 Мои записи")
async def show_bookings(msg: Message):
    sent = await msg.answer("📋 Проверяю ваши записи…")
    await show_loading(sent)
    await msg.answer("📭 У вас пока нет активных записей. Нажмите 🧹 <b>Услуги</b>, чтобы оформить новую.", parse_mode=ParseMode.HTML)

@router.message(F.text == "💬 Поддержка")
async def support(msg: Message):
    await msg.answer("💬 Напишите: @a.vcleaning_support 💎", parse_mode=ParseMode.HTML)

@router.message(F.text == "⚙️ Настройки")
async def settings(msg: Message):
    await msg.answer("⚙️ <b>Настройки профиля</b>
Скоро здесь можно будет изменить имя, адрес и телефон.", parse_mode=ParseMode.HTML)

async def run_bot():
    from os import getenv
    token = getenv("TELEGRAM_BOT_TOKEN") or "YOUR_TELEGRAM_BOT_TOKEN"
    bot = Bot(token=token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(run_bot())
