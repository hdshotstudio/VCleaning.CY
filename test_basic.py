# tests/test_basic.py — базовые проверки
from importlib import import_module

def test_router_exists():
    bot = import_module("bot")
    assert hasattr(bot, "router"), "router должен существовать"

def test_strings_present():
    bot = import_module("bot")
    assert hasattr(bot, "WELCOME"), "WELCOME строка должна существовать"