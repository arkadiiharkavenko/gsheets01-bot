import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message

import bot_app.main
from bot_app import config
from bot_app.handlers.admin.admin_echo import admin_echo_button
from bot_app.handlers.profit.handler import AddNewProfit
from bot_app.keyboard.inline_markup import expenses_button
# from bot_app.keyboard.reply_echo_admin_button import admin_cancel_button
from bot_app.keyboard.reply_cancel_button import back_cancel_btn, cancel_btn
from bot_app.misc import dp, bot


class AddNewExpense(StatesGroup):
    add_new_row = State()


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='🔚    Вийти',
                    state=AddNewExpense.add_new_row)
async def cancel_expense(message: Message, state: FSMContext):
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.delete_message(message.from_user.id, message.message_id - 1)
    await state.finish()
    await bot.send_message(chat_id=message.from_user.id, text='Додавання витрат відмінено',
                           reply_markup=admin_echo_button())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='⬅️  Назад',
                    state=AddNewExpense.add_new_row)
async def back_to_choice_expense(message: Message, state: FSMContext):
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.delete_message(message.from_user.id, message.message_id-1)
    await bot.send_message(message.from_user.id, text='Повернення в меню вибору',
                           reply_markup=bot_app.keyboard.reply_cancel_button.cancel_btn())
    await bot.send_message(chat_id=message.from_user.id, text='Виберіть категорію витрат:',
                           reply_markup=expenses_button())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='🛒')
async def choice_expense(message: Message):
    await bot.send_message(message.from_user.id, text='Вхід в меню додавання витрат',
                           reply_markup=bot_app.keyboard.reply_cancel_button.cancel_btn())
    await bot.send_message(chat_id=message.from_user.id, text='Виберіть категорію витрат:',
                           reply_markup=expenses_button())
    await AddNewExpense.add_new_row.set()


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID),
                           text_startswith='category-', state=AddNewExpense.add_new_row)
async def settings_menu(call: CallbackQuery, state: FSMContext):
    """
    Достаем имена расходов из словаря в конфиге, потом с базы данных такое будешь доставать, но пока так,
    что бы можно было легко добавить новые не сильно меня код, так же колл бек если однотипный - можно сделать стартвиз
    """
    await call.answer()

    await state.set_data({'state': call.data})
    text_for_user = config.category_names.get(call.data.split('-')[1])
    await call.message.delete()
    await bot.send_message(call.from_user.id, text=f'Обрано категорію   <b>"{text_for_user}" </b>\n\n'
                                                   f'Введіть суму витрат (без копійок):',
                           reply_markup=bot_app.keyboard.reply_cancel_button.back_cancel_btn())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID),
                    regexp='^[0-9][0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9]$|^[0-9][0-9]$|^[1-9]$',
                    state=AddNewExpense.add_new_row
                    )
async def add_new_prod(message: Message, state: FSMContext):
    summa = message.text
    user_name = message.from_user.first_name
    date_mes = message.date
    state_status = await state.get_data()
    categories = state_status['state'].split('-')[1]
    range_ = await bot_app.main.set_current_range_expenses(date_mes)

    if categories == 'products':
        values_data = [user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None,
                       summa]
    elif categories == 'services':
        values_data = [user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None,
                       None, summa]
    elif categories == 'relax':
        values_data = [user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None,
                       None, None, summa]
    elif categories == 'cleaning':
        values_data = [user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None,
                       None, None, None, summa]
    elif categories == 'car':
        values_data = [user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None,
                       None, None, None, None, summa]
    elif categories == 'village':
        values_data = [user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None,
                       None, None, None, None, None, summa]
    elif categories == 'credit':
        values_data = [user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None,
                       None, None, None, None, None, None, summa]
    else:
        values_data = [user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None,
                       None, None, None, None, None, None, None, summa]

    await bot_app.main.add_new_row(range_, {'values': [values_data]})

    await bot.send_message(message.from_user.id, text=f'Витрати успішно додано', reply_markup=cancel_btn())
    await bot.send_message(chat_id=message.from_user.id, text='Для продовдення виберіть категорію витрат,\n\n'
                                                              'для виходу  -  "🔚    Вийти"',
                           reply_markup=expenses_button())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), state=AddNewExpense)
async def add_new_row(message: Message, state: FSMContext):
    state_status = await state.get_data()
    try:
        categories = state_status['state'].split('-')[1]
    except KeyError:
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.send_message(message.from_user.id, text='Виберіть одну із запропонованих категорій  👆')
        return

    await bot.send_message(message.from_user.id, text=f'⚠  ️Помилка введення!\nВведіть ціле число або натисніть "🔚    Вийти"   👇',
                           reply_markup=bot_app.keyboard.reply_cancel_button.cancel_btn())



