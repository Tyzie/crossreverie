from vkbottle.bot import Blueprint, Message
from player import Player
from config import mainkeyb

cog = Blueprint("Registration")
cog.labeler.vbml_ignore_case = True

@cog.on.message(text=["начать", "начать <text>"])
async def help(message: Message, text='CrossReverie Player'):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False:
		pass
	if player == False:
		race = Player.create_profile(user[0].id, text)
		await message.answer(f"[id{user[0].id}|{user[0].first_name}], ты успешно зарегестрировался! Твоя раса в этом мире: {race} 🌍")