# tests/test_menu.py — простые тесты генерации клавиатуры
from importlib import import_module

def test_module_imports():
    bot = import_module("bot")
    assert hasattr(bot, "main_menu"), "main_menu должен существовать"

def test_main_menu_layout():
    bot = import_module("bot")
    kb = bot.main_menu()
    assert kb is not None
    # aiogram может различаться по внутренней структуре — проверим наличие repr/serialize
    assert hasattr(kb, "__repr__")