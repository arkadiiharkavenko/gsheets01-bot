from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def admin_echo_button():
    full_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('🛒  Додати витрати')
    button2 = KeyboardButton('💰  Додати доходи')
    button3 = KeyboardButton('📊  Статистика')
    full_kb.row(button1, button2)
    full_kb.add(button3)
    return full_kb


def admin_cancel_button():
    full_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('Відміна')
    full_kb.row(button1)
    return full_kb
