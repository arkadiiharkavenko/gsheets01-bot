import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message

import bot_app.main
from bot_app import config
from bot_app.handlers.admin.admin_echo import admin_echo_button

from bot_app.misc import dp, bot


class AddNewProfit(StatesGroup):
    new_profit = State()


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='💵')
async def choice_expense(message: Message):
    await bot.send_message(message.from_user.id, text='Вхід в меню додавання доходів',
                           reply_markup=bot_app.keyboard.reply_cancel_button.cancel_btn())
    await AddNewProfit.new_profit.set()
    await bot.send_message(chat_id=message.from_user.id, text='Введіть суму доходу:')


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID),
                    regexp='^[0-9][0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9][0-9]$|^[0-9][0-9][0-9]$|^[0-9][0-9]$|^[1-9]$',
                    state=AddNewProfit.new_profit)
async def add_profit(message: Message, state: FSMContext):
    summa = message.text
    user_name = message.from_user.first_name
    date_mes = message.date
    range_ = await bot_app.main.set_current_range_profit(date_mes)
    await bot_app.main.add_new_row(range_, {'values': [[
        user_name, date_mes.date().day, date_mes.strftime('%H;%M'), summa
    ]]})
    await bot.send_message(message.from_user.id, text=f'Доходи успішно додано', reply_markup=admin_echo_button())
    await state.finish()


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='🔚    Вийти',
                    state=AddNewProfit.new_profit)
async def cancel_expense(message: Message, state: FSMContext):
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.delete_message(message.from_user.id, message.message_id - 1)
    await state.finish()
    await bot.send_message(chat_id=message.from_user.id, text='Додавання доходів відмінено',
                           reply_markup=admin_echo_button())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), state=AddNewProfit.new_profit)
async def add_new_row(message: Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.send_message(message.from_user.id, text=f'⚠  ️Помилка введення!\nВведіть ціле число або натисніть "🔚    Вийти"   👇',
                           reply_markup=bot_app.keyboard.reply_cancel_button.cancel_btn())

