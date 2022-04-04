from vkbottle.bot import Blueprint, Message
from player import Player
from config import mainkeyb, EMPTY_KEYBOARD

cog = Blueprint("Top")
cog.labeler.vbml_ignore_case = True

@cog.on.message(text=["топ"])
async def top(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.keyb == 1:
		i = Player.top_copper(10)
		g = Player.top_copper_uid(10)
		await message.answer(f"""Топ игроков по меди 🟧:
1 - {i[0]} [{g[0]}]
2 - {i[1]} [{g[1]}]""", keyboard=mainkeyb)
		print(i)
		Player.set_action(player.uid, "main")
		print(f"{player.nickname} [{player.uid}] called 'top'")
