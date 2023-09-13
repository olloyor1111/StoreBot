from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_cats_markup(cats, back=False) -> ReplyKeyboardMarkup:
    keyboards = []
    rows = []
    for cat in cats:
        rows.append(KeyboardButton(text=cat["name"]))
    length = len(rows)
    for index in range(1, length + 1, 2):
        try:
            keyboards.append(rows[index - 1:index + 1])
        except IndexError:
            keyboards.append(rows[index - 1:])
    if back:
        keyboards.append([KeyboardButton(text="⬅️ Orqaga")])
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboards)
    return kb
