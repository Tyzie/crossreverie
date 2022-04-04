from vkbottle import Bot, load_blueprints_from_package
import psycopg2 as ps
from config import token
import time

bot = Bot(token)

for cog in load_blueprints_from_package("cogs"):
    cog.load(bot)

time.sleep(3)

bot.run_forever()
