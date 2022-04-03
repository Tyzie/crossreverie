from vkbottle.bot import Blueprint, Message
from player import Player
from config import mainkeyb

cog = Blueprint("Help")
cog.labeler.vbml_ignore_case = True

@cog.on.message(text=["помощь"])
async def help(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.keyb == 1:
		await message.answer(f"""Мои команды, [id{player.id}|{player.nickname}] [{player.uid}]
			&#12288;Профиль
			&#12288;Помощь
			&#12288;⚙ Настройки
			&#12288;Ник [новый ник]""", keyboard=mainkeyb)
		print(f"{player.nickname} [{player.uid}] called 'help'")
	if player != False and player.keyb == 0:
		await message.answer(f"""Мои команды, [id{player.id}|{player.nickname}] [{player.uid}]
			&#12288;Профиль
			&#12288;Помощь
			&#12288;⚙ Настройки
			&#12288;Ник [новый ник]""")
		print(f"{player.nickname} [{player.uid}] called 'help'")
	# 100m = 1s 1g = 100s
	