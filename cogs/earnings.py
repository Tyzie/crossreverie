from vkbottle.bot import Blueprint, Message
from player import Player
from config import mainkeyb

cog = Blueprint("Earnings")
cog.labeler.vbml_ignore_case = True

@cog.on.message(text=["заработок"])
async def earnings(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	