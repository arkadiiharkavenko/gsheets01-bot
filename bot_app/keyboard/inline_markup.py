from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def expenses_button():
    inline_btn_1 = InlineKeyboardButton('🥪  Продукти',
                                        callback_data='products')

    inline_btn_2 = InlineKeyboardButton('🏢 💡 🚰  Комуналка',
                                        callback_data='services')

    inline_btn_3 = InlineKeyboardButton('🏝️  Відпочинок',
                                        callback_data='relax')

    inline_btn_4 = InlineKeyboardButton('🪥  🛁  Засоби миття та гігієни',
                                        callback_data='cleaning')

    inline_btn_5 = InlineKeyboardButton('🚗  Витрати на авто',
                                        callback_data='car')

    inline_btn_6 = InlineKeyboardButton('🏡  Витрати на село',
                                        callback_data='village')

    inline_btn_7 = InlineKeyboardButton('💳  Погашення кредиту',
                                        callback_data='credit')

    inline_btn_8 = InlineKeyboardButton('💅🏻 👨 ‍🦲 ♨️ 📚   Інше',
                                        callback_data='other')
    #
    inline_btn_9 = InlineKeyboardButton('Відміна', callback_data='cancellation')

    inline_kb_full = InlineKeyboardMarkup(row_width=1)
    inline_kb_full.add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4, inline_btn_5,
                       inline_btn_6, inline_btn_7, inline_btn_8, inline_btn_9)
    return inline_kb_full


def cancellation():
    inline_kb_full = InlineKeyboardMarkup(row_width=1)
    inline_kb_full.add(InlineKeyboardButton(text='Відміна', callback_data=f'cancellation'))
    return inline_kb_full


def back_action():
    inline_kb_full = InlineKeyboardMarkup(row_width=1)
    inline_kb_full.add(InlineKeyboardButton(text='⬅️  Назад', callback_data='back-to'))
    return inline_kb_full


def back_and_cancel():
    inline_kb_full = InlineKeyboardMarkup(row_width=2)
    inline_btn_1 = InlineKeyboardButton(text='⬅️  Назад', callback_data='back-to-choice')
    inline_btn_2 = InlineKeyboardButton(text='Відміна', callback_data=f'cancellation')
    inline_kb_full.add(inline_btn_1, inline_btn_2)
    return inline_kb_full


def change_month():
    inline_kb_full = InlineKeyboardMarkup(row_width=4)
    inline_btn_1 = InlineKeyboardButton('Поточний місяць', callback_data='current')
    inline_btn_2 = InlineKeyboardButton('Cічень', callback_data='January')
    inline_btn_3 = InlineKeyboardButton('Лютий', callback_data='February')
    inline_btn_4 = InlineKeyboardButton('Березень', callback_data='March')
    inline_btn_5 = InlineKeyboardButton('Квітень', callback_data='April')
    inline_btn_6 = InlineKeyboardButton('Травень', callback_data='May')
    inline_btn_7 = InlineKeyboardButton('Червень', callback_data='June')
    inline_btn_8 = InlineKeyboardButton('Липень', callback_data='July')
    inline_btn_9 = InlineKeyboardButton('Серпень', callback_data='August')
    inline_btn_10 = InlineKeyboardButton('Вересень', callback_data='September')
    inline_btn_11 = InlineKeyboardButton('Жовтень', callback_data='October')
    inline_btn_12 = InlineKeyboardButton('Листопад', callback_data='November')
    inline_btn_13 = InlineKeyboardButton('Грудень', callback_data='December')
    inline_btn_14 = InlineKeyboardButton('За рік', callback_data='2022')
    inline_btn_16 = InlineKeyboardButton('Відміна', callback_data='cancellation')
    inline_btn_15 = InlineKeyboardButton('Відкрити таблицю з даними',
                                         url='https://docs.google.com/spreadsheets/d/1qiWzy1pj8g2i0f-'
                                             'klSqWXh66QbuBJBnBQVviZiknWMI/edit#gid=2070221350')
    inline_kb_full.row(inline_btn_1)
    inline_kb_full.add(inline_btn_2, inline_btn_3, inline_btn_4, inline_btn_5, inline_btn_6, inline_btn_7,
                       inline_btn_8, inline_btn_9, inline_btn_10, inline_btn_11, inline_btn_12, inline_btn_13)
    inline_kb_full.row(inline_btn_14)
    inline_kb_full.row(inline_btn_15)
    inline_kb_full.row(inline_btn_16)

    return inline_kb_full

