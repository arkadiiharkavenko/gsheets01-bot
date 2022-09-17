import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message

import bot_app.main
from bot_app import config
from bot_app.handlers.admin.admin_echo import admin_echo_button
from bot_app.handlers.profit.handler import AddNewProfit
from bot_app.keyboard.inline_markup import expenses_button, cancellation
from bot_app.keyboard.reply_echo_admin_button import admin_cancel_button
from bot_app.misc import dp, bot


class AddNewExpense(StatesGroup):
    add_new_row = State()


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text=['cancellation', 'back-to'],
                           state='*')
async def settings_menu(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.delete_reply_markup()
    await state.finish()
    await call.message.edit_text(text='Дію відмінено')


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='Відміна', state='*')
async def choice_expense(message: Message, state: FSMContext):
    await state.finish()
    await bot.send_message(chat_id=message.from_user.id, text='Дію відмінено',
                           reply_markup=admin_echo_button())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='🛒  Додати витрати')
async def choice_expense(message: Message):
    await bot.send_message(chat_id=message.from_user.id, text='Виберіть категорію витрат:',
                           reply_markup=expenses_button())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID),
                           text=['products', 'services', 'relax', 'cleaning', 'car', 'village', 'credit', 'other'])
async def settings_menu(call: CallbackQuery, state: FSMContext):
    await call.answer()
    categories = call.data
    await AddNewExpense.add_new_row.set()
    if categories == 'products':
        text_for_user = 'Продукти'
        await state.set_data({'state': 'products'})
    elif categories == 'services':
        text_for_user = 'Комуналка'
        await state.set_data({'state': 'services'})
    elif categories == 'relax':
        text_for_user = 'Відпочинок'
        await state.set_data({'state': 'relax'})
    elif categories == 'cleaning':
        text_for_user = 'Засоби миття та гігієни'
        await state.set_data({'state': 'cleaning'})
    elif categories == 'car':
        text_for_user = 'Витрати на авто'
        await state.set_data({'state': 'car'})
    elif categories == 'village':
        text_for_user = 'Витрати на село'
        await state.set_data({'state': 'village'})
    elif categories == 'credit':
        text_for_user = 'Погашення кредиту'
        await state.set_data({'state': 'credit'})
    else:
        text_for_user = 'Інше'
        await state.set_data({'state': 'other'})

    await call.message.edit_text(text=f'Обрано категорію "{text_for_user}"\nВведіть суму витрат (без копійок):',
                                 reply_markup=cancellation())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID),
                    regexp='^[0-9][0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9]$|^[0-9][0-9]$|^[0-9]$',
                    state=AddNewExpense.add_new_row
                    )
async def add_new_prod(message: Message, state: FSMContext):
    summa = message.text
    user_name = message.from_user.first_name
    date_mes = message.date
    state_status = await state.get_data()
    range_ = await bot_app.main.set_current_range_expenses(date_mes)

    if state_status['state'] == 'products':
        values_data = [user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None,
                       summa, None, None, None, None, None, None, None]
    elif state_status['state'] == 'services':
        values_data = [user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None,
                       None, summa, None, None, None, None, None, None]
    elif state_status['state'] == 'relax':
        values_data = [user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None,
                       None, None, summa, None, None, None, None, None]
    elif state_status['state'] == 'cleaning':
        values_data = [user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None,
                       None, None, None, summa, None, None, None, None]
    elif state_status['state'] == 'car':
        values_data = [user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None,
                       None, None, None, None, summa, None, None, None]
    elif state_status['state'] == 'village':
        values_data = [user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None,
                       None, None, None, None, None, summa, None, None]
    elif state_status['state'] == 'credit':
        values_data = [user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None,
                       None, None, None, None, None, None, summa, None]
    else:
        values_data = [user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None,
                       None, None, None, None, None, None, None, summa]

    await bot_app.main.add_new_row(range_, {'values': [values_data]})

    await bot.send_message(message.from_user.id, text=f'Витрати успішно додано', reply_markup=admin_echo_button())
    await state.finish()


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), state=[AddNewExpense, AddNewProfit])
async def add_new_row(message: Message):
    await bot.send_message(message.from_user.id, text=f'Помилка введення!\nВведіть ціле число або натисніть "Відміна" 👇',
                           reply_markup=admin_cancel_button())



