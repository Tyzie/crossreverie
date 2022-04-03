from vkbottle.bot import Blueprint, Message
from player import Player
from config import mainkeyb

cog = Blueprint("Registration")
cog.labeler.vbml_ignore_case = True

@cog.on.message(text=["начать", "начать <text>"])
async def reg(message: Message, text='CrossReverie Player'):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player == False:
		race = Player.create_profile(user[0].id, text)
		await message.answer(f"[id{user[0].id}|{user[0].first_name}], ты успешно зарегестрировался! Твоя раса в этом мире: {race} 🌍", keyboard=mainkeyb)
		print(f"{user[0].id} registered in bot!")
	if player != False and player.keyb == 1:
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], ты уже зарегестрирован в боте! ❌", keyboard=mainkeyb)
		print(f"{player.nickname} [{player.uid}] called 'reg'")
	if player != False and player.keyb == 0:
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], ты уже зарегестрирован в боте! ❌")
		print(f"{player.nickname} [{player.uid}] called 'reg'")