import aiogram
from aiogram.types import CallbackQuery, Message

import bot_app.main
from bot_app import config
from bot_app.keyboard.inline_markup import change_month, back_and_cancel
from bot_app.misc import dp, bot


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='back-to-choice')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.edit_reply_markup(reply_markup=change_month())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='📊  Статистика')
async def choice_statistic(message: Message):
    await bot.send_message(chat_id=message.from_user.id, text='Виберіть період:',
                           reply_markup=change_month())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID),
                           text=['current', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                                 'September', 'October', 'November', 'December', '2022'])
async def settings_menu(call: CallbackQuery):
    await call.answer()
    date_mes = call.message.date
    mouth = call.data
    await call.message.delete_reply_markup()
    if mouth == 'current':
        text_for_user = 'поточному місяці'
        mouth = date_mes.strftime('%B')
    elif mouth == 'January':
        text_for_user = 'січні'
    elif mouth == 'February':
        text_for_user = 'лютому'
    elif mouth == 'March':
        text_for_user = 'березні'
    elif mouth == 'April':
        text_for_user = 'квітні'
    elif mouth == 'May':
        text_for_user = 'травні'
    elif mouth == 'June':
        text_for_user = 'червні'
    elif mouth == 'July':
        text_for_user = 'липні'
    elif mouth == 'August':
        text_for_user = 'серпні'
    elif mouth == 'September':
        text_for_user = 'вересні'
    elif mouth == 'October':
        text_for_user = 'жовтні'
    elif mouth == 'November':
        text_for_user = 'листопаді'
    elif mouth == 'December':
        text_for_user = 'грудні'
    else:
        text_for_user = '2022 році'

    if mouth == '2022':
        result = await bot_app.main.get_data_for_year('2022')
    else:
        result = await bot_app.main.get_data_for_month(mouth)

    await call.message.edit_text(text=f'У {text_for_user} зароблено та витрачено:\n'
                                      f'{result}',
                                 reply_markup=back_and_cancel())


@dp.message_handler(aiogram.filters.ChatTypeFilter(aiogram.types.ChatType.PRIVATE))
async def eny_text_messages(message: Message):
    if message.from_user.id not in config.ADMINS_ID:
        await bot.send_message(chat_id=message.from_user.id, text='Ви не адмін данного бота!')
        return
    await bot.send_message(chat_id=message.from_user.id,
                           text='Упс! незрозуміла команда\nМожливо ви мали на увазі: /start або /admin')