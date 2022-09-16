import aiogram
from aiogram.types import CallbackQuery, Message, ParseMode

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


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='current')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    date_mes = call.message.date
    await call.message.delete_reply_markup()
    result = await bot_app.main.get_data_for_cur_month(date_mes)
    await call.message.edit_text(text='У поточному місяці зароблено та витрачено:\n'
                                      f'{result}',
                                 reply_markup=back_and_cancel())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='january')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    result = await bot_app.main.get_data_for_month('January')
    await call.message.edit_text(text='У січні зароблено та витрачено:\n'
                                      f'{result}',
                                 reply_markup=back_and_cancel())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='february')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    result = await bot_app.main.get_data_for_month('February')
    await call.message.edit_text(text='У лютому зароблено та витрачено:\n'
                                      f'{result}',
                                 reply_markup=back_and_cancel())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='march')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    result = await bot_app.main.get_data_for_month('March')
    await call.message.edit_text(text='У березні зароблено та витрачено:\n'
                                      f'{result}',
                                 reply_markup=back_and_cancel())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='april')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    result = await bot_app.main.get_data_for_month('April')
    await call.message.edit_text(text='У квітні зароблено та витрачено:\n'
                                      f'{result}',
                                 reply_markup=back_and_cancel())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='may')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    result = await bot_app.main.get_data_for_month('May')
    await call.message.edit_text(text='У травні зароблено та витрачено:\n'
                                      f'{result}',
                                 reply_markup=back_and_cancel())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='june')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    result = await bot_app.main.get_data_for_month('June')
    await call.message.edit_text(text='У червні зароблено та витрачено:\n'
                                      f'{result}',
                                 reply_markup=back_and_cancel())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='july')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    result = await bot_app.main.get_data_for_month('July')
    await call.message.edit_text(text='У липні зароблено та витрачено:\n'
                                      f'{result}',
                                 reply_markup=back_and_cancel())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='august')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    result = await bot_app.main.get_data_for_month('August')
    await call.message.edit_text(text='У серпні зароблено та витрачено:\n'
                                      f'{result}',
                                 reply_markup=back_and_cancel())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='september')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    result = await bot_app.main.get_data_for_month('September')
    await call.message.edit_text(text='У вересні зароблено та витрачено:\n'
                                      f'{result}',
                                 reply_markup=back_and_cancel())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='october')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    result = await bot_app.main.get_data_for_month('October')
    await call.message.edit_text(text='У жовтні зароблено та витрачено:\n'
                                      f'{result}',
                                 reply_markup=back_and_cancel())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='november')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    result = await bot_app.main.get_data_for_month('November')
    await call.message.edit_text(text='У листопаді зароблено та витрачено:\n'
                                      f'{result}',
                                 reply_markup=back_and_cancel())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='december')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    result = await bot_app.main.get_data_for_month('December')
    await call.message.edit_text(text='У грудні зароблено та витрачено:\n'
                                      f'{result}',
                                 reply_markup=back_and_cancel())


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='year')
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    result = await bot_app.main.get_data_for_year('2022')
    await call.message.edit_text(text='У 2022 році зароблено та витрачено:\n'
                                      f'{result}',
                                 reply_markup=back_and_cancel())


@dp.message_handler(aiogram.filters.ChatTypeFilter(aiogram.types.ChatType.PRIVATE))
async def eny_text_messages(message: Message):
    if message.from_user.id not in config.ADMINS_ID:
        await bot.send_message(chat_id=message.from_user.id, text='Ви не адмін данного бота!')
        return
    await bot.send_message(chat_id=message.from_user.id,
                           text='Упс! незрозуміла команда\nМожливо ви мали на увазі: /start або /admin')