from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def expenses_button():
    inline_btn_1 = InlineKeyboardButton('🥪  Продукти',
                                        callback_data='category-products')

    inline_btn_2 = InlineKeyboardButton('🏢 💡 🚰  Комуналка',
                                        callback_data='category-services')

    inline_btn_3 = InlineKeyboardButton('🏝️  Відпочинок',
                                        callback_data='category-relax')

    inline_btn_4 = InlineKeyboardButton('🪥  🛁  Засоби миття та гігієни',
                                        callback_data='category-cleaning')

    inline_btn_5 = InlineKeyboardButton('🚗  Витрати на авто',
                                        callback_data='category-car')

    inline_btn_6 = InlineKeyboardButton('🏡  Витрати на село',
                                        callback_data='category-village')

    inline_btn_7 = InlineKeyboardButton('💳  Погашення кредиту',
                                        callback_data='category-credit')

    inline_btn_8 = InlineKeyboardButton('💅🏻 👨 ‍🦲 ♨️ 📚   Інше',
                                        callback_data='category-other')
    inline_kb_full = InlineKeyboardMarkup(row_width=1)
    inline_kb_full.add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4, inline_btn_5,
                       inline_btn_6, inline_btn_7, inline_btn_8)
    return inline_kb_full

#
# def cancellation():
#     inline_kb_full = InlineKeyboardMarkup(row_width=1)
#     inline_kb_full.add(InlineKeyboardButton(text='Відміна', callback_data=f'cancellation'))
#     return inline_kb_full


def back_action():
    inline_kb_full = InlineKeyboardMarkup(row_width=1)
    inline_kb_full.add(InlineKeyboardButton(text='⬅️  Назад', callback_data='back-to'))
    return inline_kb_full


def back_and_cancel():
    inline_kb_full = InlineKeyboardMarkup(row_width=2)
    inline_btn_1 = InlineKeyboardButton(text='⬅️  Назад', callback_data='back-to-choice')
    inline_kb_full.add(inline_btn_1)
    return inline_kb_full


def change_month():
    inline_kb_full = InlineKeyboardMarkup(row_width=4)
    inline_btn_1 = InlineKeyboardButton('Поточний місяць', callback_data='mouth-current')
    inline_btn_2 = InlineKeyboardButton('Cічень', callback_data='mouth-January')
    inline_btn_3 = InlineKeyboardButton('Лютий', callback_data='mouth-February')
    inline_btn_4 = InlineKeyboardButton('Березень', callback_data='mouth-March')
    inline_btn_5 = InlineKeyboardButton('Квітень', callback_data='mouth-April')
    inline_btn_6 = InlineKeyboardButton('Травень', callback_data='mouth-May')
    inline_btn_7 = InlineKeyboardButton('Червень', callback_data='mouth-June')
    inline_btn_8 = InlineKeyboardButton('Липень', callback_data='mouth-July')
    inline_btn_9 = InlineKeyboardButton('Серпень', callback_data='mouth-August')
    inline_btn_10 = InlineKeyboardButton('Вересень', callback_data='mouth-September')
    inline_btn_11 = InlineKeyboardButton('Жовтень', callback_data='mouth-October')
    inline_btn_12 = InlineKeyboardButton('Листопад', callback_data='mouth-November')
    inline_btn_13 = InlineKeyboardButton('Грудень', callback_data='mouth-December')
    inline_btn_14 = InlineKeyboardButton('За рік', callback_data='mouth-YEAR')
    inline_btn_15 = InlineKeyboardButton('Відкрити таблицю з даними',
                                         url='https://docs.google.com/spreadsheets/d/1qiWzy1pj8g2i0f-'
                                             'klSqWXh66QbuBJBnBQVviZiknWMI/edit#gid=2070221350')
    inline_kb_full.row(inline_btn_1)
    inline_kb_full.add(inline_btn_2, inline_btn_3, inline_btn_4, inline_btn_5, inline_btn_6, inline_btn_7,
                       inline_btn_8, inline_btn_9, inline_btn_10, inline_btn_11, inline_btn_12, inline_btn_13)
    inline_kb_full.row(inline_btn_14)
    inline_kb_full.row(inline_btn_15)

    return inline_kb_full

