from aiogram import executor
from aiogram.types import AllowedUpdates

from bot_app.misc import dp


if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True, allowed_updates=AllowedUpdates.MESSAGE + AllowedUpdates.CHAT_MEMBER +
                           AllowedUpdates.CALLBACK_QUERY + AllowedUpdates.MY_CHAT_MEMBER + AllowedUpdates.CHAT_JOIN_REQUEST)
