from asyncio import get_event_loop

import aioredis
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from bot_app.config import BOT_TOKEN, REDIS

loop = get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
storage = RedisStorage2(**REDIS, loop=loop)
dp = Dispatcher(bot, loop, storage)
redis = aioredis.Redis(decode_responses=True)

