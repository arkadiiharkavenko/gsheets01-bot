from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def cancel_btn():
    full_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    full_kb.row(KeyboardButton('Отмена'))
    return full_kb
