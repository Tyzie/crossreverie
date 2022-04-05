from vkbottle import Bot, load_blueprints_from_package
import psycopg2 as ps
from config import token, DB_URI
import os
import time
import asyncio

bot = Bot(token)

for cog in load_blueprints_from_package("cogs"):
    cog.load(bot)

bot.run_forever()
