import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message

import bot_app.main
from bot_app import config
from bot_app.handlers.admin.admin_echo import admin_echo_button
from bot_app.keyboard.inline_markup import expenses_button, cancellation
from bot_app.keyboard.reply_echo_admin_button import admin_cancel_button
from bot_app.misc import dp, bot


class AddNewExpense(StatesGroup):
    expense_prod = State()
    expense_service = State()
    expense_relax = State()
    expense_clean = State()
    expense_car = State()
    expense_village = State()
    expense_credit = State()
    expense_other = State()


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='cancellation', state='*')
async def settings_menu(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.delete_reply_markup()
    await state.finish()
    await call.message.edit_text(text='Дію відмінено')


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='back-to', state='*')
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
                           reply_markup=expenses_button(message.chat.id))


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text_startswith='products')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    await AddNewExpense.expense_prod.set()
    await call.message.edit_text(text='Обрано категорію "Продукти"\nВведіть суму витрат (без копійок):',
                                 reply_markup=cancellation())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text_startswith='services')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    await AddNewExpense.expense_service.set()
    await call.message.edit_text(text='Обрано категорію "Комуналка"\nВведіть суму витрат (без копійок):',
                                 reply_markup=cancellation())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text_startswith='relax')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    await AddNewExpense.expense_relax.set()
    await call.message.edit_text(text='Обрано категорію "Відпочинок"\nВведіть суму витрат (без копійок):',
                                 reply_markup=cancellation())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text_startswith='cleaning')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    await AddNewExpense.expense_clean.set()
    await call.message.edit_text(text='Обрано категорію "Засоби миття та гігієни"\nВведіть суму витрат (без копійок):',
                                 reply_markup=cancellation())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text_startswith='car')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    await AddNewExpense.expense_car.set()
    await call.message.edit_text(text='Обрано категорію "Витрати на авто"\nВведіть суму витрат (без копійок):',
                                 reply_markup=cancellation())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text_startswith='village')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    await AddNewExpense.expense_village.set()
    await call.message.edit_text(text='Обрано категорію "Витрати на село"\nВведіть суму витрат (без копійок):',
                                 reply_markup=cancellation())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text_startswith='credit')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    await AddNewExpense.expense_credit.set()
    await call.message.edit_text(text='Обрано категорію "Погашення кредиту"\nВведіть суму витрат (без копійок):',
                                 reply_markup=cancellation())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text_startswith='other')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    await AddNewExpense.expense_other.set()
    await call.message.edit_text(text='Обрано категорію "Інше"\nВведіть суму витрат (без копійок):',
                                 reply_markup=cancellation())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID),
                    regexp='^[0-9][0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9]$|^[0-9][0-9]$|^[0-9]$',
                    state=AddNewExpense.expense_prod)
async def add_new_prod(message: Message, state: FSMContext):

    summa = message.text
    user_name = message.from_user.first_name
    date_mes = message.date
    range_ = await bot_app.main.set_current_range_expenses(date_mes)
    await bot_app.main.add_new_row(range_, {'values': [[
        user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None, summa, None, None, None, None, None, None, None
    ]]})
    await bot.send_message(message.from_user.id, text=f'Витрати успішно додано', reply_markup=admin_echo_button())
    await state.finish()


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), state=AddNewExpense.expense_prod)
async def add_new_prod(message: Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text=f'Помилка введення!\nВведіть ціле число або натисніть "Відміна" 👇',
                           reply_markup=admin_cancel_button())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID),
                    regexp='^[0-9][0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9]$|^[0-9][0-9]$|^[0-9]$',
                    state=AddNewExpense.expense_service)
async def add_new_service(message: Message, state: FSMContext):
    summa = message.text
    user_name = message.from_user.first_name
    date_mes = message.date
    range_ = await bot_app.main.set_current_range_expenses(date_mes)
    await bot_app.main.add_new_row(range_, {'values': [[
        user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None, None, summa, None, None, None, None, None, None
    ]]})
    await bot.send_message(message.from_user.id, text=f'Витрати успішно додано', reply_markup=admin_echo_button())
    await state.finish()


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), state=AddNewExpense.expense_service)
async def add_new_prod(message: Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text=f'Помилка введення!\nВведіть ціле число або натисніть "Відміна" 👇',
                           reply_markup=admin_cancel_button())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID),
                    regexp='^[0-9][0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9]$|^[0-9][0-9]$|^[0-9]$',
                    state=AddNewExpense.expense_car)
async def add_new_car(message: Message, state: FSMContext):
    summa = message.text
    user_name = message.from_user.first_name
    date_mes = message.date
    range_ = await bot_app.main.set_current_range_expenses(date_mes)
    await bot_app.main.add_new_row(range_, {'values': [[
        user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None, None, None, None, None, summa, None, None, None
    ]]})
    await bot.send_message(message.from_user.id, text=f'Витрати успішно додано', reply_markup=admin_echo_button())
    await state.finish()


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), state=AddNewExpense.expense_car)
async def add_new_prod(message: Message):
    await bot.send_message(message.from_user.id, text=f'Помилка введення!\nВведіть ціле число або натисніть "Відміна" 👇',
                           reply_markup=admin_cancel_button())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID),
                    regexp='^[0-9][0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9]$|^[0-9][0-9]$|^[0-9]$',
                    state=AddNewExpense.expense_relax)
async def add_new_relax(message: Message, state: FSMContext):
    summa = message.text
    user_name = message.from_user.first_name
    date_mes = message.date
    range_ = await bot_app.main.set_current_range_expenses(date_mes)
    await bot_app.main.add_new_row(range_, {'values': [[
        user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None, None, None, summa, None, None, None, None, None
    ]]})
    await bot.send_message(message.from_user.id, text=f'Витрати успішно додано', reply_markup=admin_echo_button())
    await state.finish()


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), state=AddNewExpense.expense_relax)
async def add_new_prod(message: Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text=f'Помилка введення!\nВведіть ціле число або натисніть "Відміна" 👇',
                           reply_markup=admin_cancel_button())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID),
                    regexp='^[0-9][0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9]$|^[0-9][0-9]$|^[0-9]$',
                    state=AddNewExpense.expense_clean)
async def add_new_clean(message: Message, state: FSMContext):
    summa = message.text
    user_name = message.from_user.first_name
    date_mes = message.date
    range_ = await bot_app.main.set_current_range_expenses(date_mes)
    await bot_app.main.add_new_row(range_, {'values': [[
        user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None, None, None, None, summa, None, None, None, None
    ]]})
    await bot.send_message(message.from_user.id, text=f'Витрати успішно додано', reply_markup=admin_echo_button())
    await state.finish()


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), state=AddNewExpense.expense_clean)
async def add_new_prod(message: Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text=f'Помилка введення!\nВведіть ціле число або натисніть "Відміна" 👇',
                           reply_markup=admin_cancel_button())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID),
                    regexp='^[0-9][0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9]$|^[0-9][0-9]$|^[0-9]$',
                    state=AddNewExpense.expense_credit)
async def add_new_credit(message: Message, state: FSMContext):
    summa = message.text
    user_name = message.from_user.first_name
    date_mes = message.date
    range_ = await bot_app.main.set_current_range_expenses(date_mes)
    await bot_app.main.add_new_row(range_, {'values': [[
        user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None, None, None, None, None, None, None, summa, None
    ]]})
    await bot.send_message(message.from_user.id, text=f'Витрати успішно додано', reply_markup=admin_echo_button())
    await state.finish()


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), state=AddNewExpense.expense_credit)
async def add_new_prod(message: Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text=f'Помилка введення!\nВведіть ціле число або натисніть "Відміна" 👇',
                           reply_markup=admin_cancel_button())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID),
                    regexp='^[0-9][0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9]$|^[0-9][0-9]$|^[0-9]$',
                    state=AddNewExpense.expense_village)
async def add_new_village(message: Message, state: FSMContext):
    summa = message.text
    user_name = message.from_user.first_name
    date_mes = message.date
    range_ = await bot_app.main.set_current_range_expenses(date_mes)
    await bot_app.main.add_new_row(range_, {'values': [[
        user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None, None, None, None, None, None, summa, None, None
    ]]})
    await bot.send_message(message.from_user.id, text=f'Витрати уснішно додано', reply_markup=admin_echo_button())
    await state.finish()


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), state=AddNewExpense.expense_village)
async def add_new_prod(message: Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text=f'Помилка введення!\nВведіть ціле число або натисніть "Відміна" 👇',
                           reply_markup=admin_cancel_button())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID),
                    regexp='^[0-9][0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9]$|^[0-9][0-9]$|^[0-9]$',
                    state=AddNewExpense.expense_other)
async def add_new_other(message: Message, state: FSMContext):
    summa = message.text
    user_name = message.from_user.first_name
    date_mes = message.date
    range_ = await bot_app.main.set_current_range_expenses(date_mes)
    await bot_app.main.add_new_row(range_, {'values': [[
        user_name, date_mes.date().day, date_mes.strftime('%H;%M'), None, None, None, None, None, None, None, None, summa
    ]]})
    await bot.send_message(message.from_user.id, text=f'Витрати успішно додано', reply_markup=admin_echo_button())
    await state.finish()


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), state=AddNewExpense.expense_other)
async def add_new_prod(message: Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text=f'Помилка введення!\nВведіть ціле число або натисніть "Відміна" 👇',
                           reply_markup=admin_cancel_button())



