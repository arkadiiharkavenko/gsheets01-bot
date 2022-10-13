from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def cancel_btn():
    full_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    full_kb.row(KeyboardButton('🔚    Вийти'))
    return full_kb

def back_cancel_btn():
    full_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    full_kb.row(KeyboardButton('⬅️  Назад'))
    return full_kb


def exit_stat():
    full_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    full_kb.row(KeyboardButton('🔚    Вийти'))
    return full_kb