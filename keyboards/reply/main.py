from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_cats_markup(cats) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for cat in cats:
        kb.add(KeyboardButton(text=cat["name"]))
    kb.adjust(2)
    return kb.as_markup(resize_keyboard = True)
