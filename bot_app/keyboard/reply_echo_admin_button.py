from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def admin_echo_button():
    full_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('๐')
    button2 = KeyboardButton('๐ต')
    button3 = KeyboardButton('๐')
    full_kb.row(button1, button2, button3)
    # full_kb.add(button3)
    return full_kb


# def admin_cancel_button():
#     full_kb = ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = KeyboardButton('ะัะดะผัะฝะฐ')
#     full_kb.row(button1)
#     return full_kb
