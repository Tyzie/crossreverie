from vkbottle.bot import Blueprint, Message
from player import Player
from config import mainkeyb

cog = Blueprint("Help")
cog.labeler.vbml_ignore_case = True

@cog.on.message(text=["профиль"])
async def help(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False:
		await message.answer(f"""Твой профиль, [id{player.id}|{player.nickname}] [{player.uid}]
			Игровой ID: {player.uid} 🆔
			Здоровье: {player.health}/{player.maxhealth} ❤
			Игровая раса: {player.race} 🌍
			Уровень: {player.level} 🔰
			Опыт: {player.xp}/{player.maxxp} ⭐
			Золото/Серебро/Медь: {player.gold} 🟡/{player.silver} ⚪/{player.copper} 🟠
			Дата регистрации в боте: {player.dater} ⌚""")
