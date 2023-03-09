import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message

import bot_app.main
from bot_app import config
from bot_app.keyboard.inline_markup import change_month, back_and_cancel
from bot_app.misc import dp, bot


class ShowStatistic(StatesGroup):
    enter_show = State()


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='back-to-choice',
                           state=ShowStatistic.enter_show)
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.edit_reply_markup(reply_markup=change_month())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='📊')
async def choice_statistic(message: Message):
    await bot.send_message(message.from_user.id, text='Вхід в меню перегляду статистики',
                           reply_markup=bot_app.keyboard.reply_cancel_button.exit_stat())
    await bot.send_message(chat_id=message.from_user.id, text='Виберіть період:',
                           reply_markup=change_month())
    await ShowStatistic.enter_show.set()


@dp.callback_query_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text_startswith='mouth-',
                           state=ShowStatistic.enter_show)
async def settings_menu(call: CallbackQuery):
    await call.answer()
    await call.message.delete_reply_markup()
    date_mes = call.message.date
    mouth = call.data.split('-')[1]
    text_for_user = config.mouth_names.get(mouth)
    if mouth == 'current':
        mouth = date_mes.strftime('%B')
    if mouth == '2022':
        result = await bot_app.main.get_data_for_year('2023')
    else:
        result = await bot_app.main.get_data_for_month(mouth)

    await call.message.edit_text(text=f'У {text_for_user} зароблено та витрачено:\n'
                                      f'{result}',
                                 reply_markup=back_and_cancel())


@dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID), text='🔚    Вийти',
                    state=ShowStatistic.enter_show)
async def exit_stat(message: Message, state: FSMContext):
    await state.finish()
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.delete_message(message.from_user.id, message.message_id - 1)
    await bot.send_message(chat_id=message.from_user.id, text='Вихід з меню перегляду статистики',
                           reply_markup=bot_app.keyboard.reply_echo_admin_button.admin_echo_button())



# @dp.message_handler(aiogram.filters.IDFilter(user_id=config.ADMINS_ID),
#                     state=ShowStatistic.enter_show)
# async def exit_stat(message: Message):
#     await bot.delete_message(message.from_user.id, message.message_id)
#


@dp.message_handler(aiogram.filters.ChatTypeFilter(aiogram.types.ChatType.PRIVATE))
async def eny_text_messages(message: Message):
    if message.from_user.id not in config.ADMINS_ID:
        await bot.send_message(chat_id=message.from_user.id, text='Ви не адмін данного бота!')
        return
    await bot.send_message(chat_id=message.from_user.id,
                           text='Упс! незрозуміла команда\nМожливо ви мали на увазі: /start або /admin')





