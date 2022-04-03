from vkbottle.bot import Blueprint, Message
from player import Player
from config import mainkeyb

cog = Blueprint("Help")
cog.labeler.vbml_ignore_case = True

@cog.on.message(text=["помощь"])
async def help(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	await message.answer(f"""Мои команды, [id{player.id}|{player.nickname}] [{player.uid}]
		&#12288;Профиль
		&#12288;Помощь""", keyboard=mainkeyb)
	