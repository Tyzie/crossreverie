from vkbottle import API, load_blueprints_from_package, ABCResponseValidator, ABCRequestValidator
from typing import Any, NoReturn, Union
from vkbottle.bot import Bot
import psycopg2 as ps
from config import token, DB_URI
import os
import time
import asyncio

bot = Bot(token)
api = API(token)

for cog in load_blueprints_from_package("cogs"):
    cog.load(bot)

class SomeResponseValidator(ABCResponseValidator):
    async def validate(self, response: dict) -> Union[Any, NoReturn]:
        # some stuff with response
        return response

class SomeRequestValidator(ABCRequestValidator):
    async def validate(self, request: dict) -> dict:
        # some stuff with request data
        return request

bot.run_forever()
api.response_validators.append(SomeResponseValidator())
api.request_validators.append(SomeRequestValidator())
