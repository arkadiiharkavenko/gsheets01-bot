# import aiogram.types
import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot_app import config
from bot_app.keyboard.reply_echo_admin_button import admin_echo_button
from bot_app.misc import dp, bot


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), commands=['admin', 'start'], state='*')
async def admin_echo(message: Message, state: FSMContext):
    await state.finish()
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Привіт {message.from_user.username}!\n'
                                f'Я - бот-бюджетник) допомагаю контролювати '
                                f'доходи та витрати для чого зберігаю всі передані мені дані у google-таблиці',
                           reply_markup=admin_echo_button())

#



