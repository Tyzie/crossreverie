from vkbottle.bot import Blueprint, Message
from player import Player
from config import mainkeyb

cog = Blueprint("Help")
cog.labeler.vbml_ignore_case = True

@cog.on.message(text=["профиль"])
async def help(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.race == "Человек":
		await message.answer(f"""Твой профиль, [id{player.id}|{player.nickname}] [{player.uid}]
📒 Игровой ID: {player.uid} 
❤ Здоровье: {player.health}/{player.maxhealth}
🌍 Игровая раса: {player.race}
💠 Уровень: {player.level}
⭐ Опыт: {player.xp}/{player.maxxp} 
🟨 Золото: {player.gold}
⬜ Серебро: {player.silver} 
🟧 Медь: {player.copper}
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
🔒 Имущество:
	&#12288;🏠 Дом: скоро!
	&#12288;🐎 Конь: скоро!
	&#12288;💼 Бизнес: скоро!

Дата регистрации в боте: {player.dater} ⌚""")
	if player != False and player.race == "Демон":
		await message.answer(f"""Твой профиль, [id{player.id}|{player.nickname}] [{player.uid}]
📒 Игровой ID: {player.uid} 
💜 Здоровье: {player.health}/{player.maxhealth}
😈 Игровая раса: {player.race}
⚛ Манна: скоро!
💠 Уровень: {player.level}
⭐ Опыт: {player.xp}/{player.maxxp} 
🟨 Золото: {player.gold}
⬜ Серебро: {player.silver} 
🟧 Медь: {player.copper}
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
🔒 Имущество:
	&#12288;🏠 Дом: скоро!
	&#12288;🐎 Конь: скоро!
	&#12288;💼 Бизнес: скоро!

Дата регистрации в боте: {player.dater} ⌚""")
