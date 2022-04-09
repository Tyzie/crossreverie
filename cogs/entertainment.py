from vkbottle.bot import Blueprint, Message
from player import Player
from config import mainkeyb, entkeyb, casinokeyb, EMPTY_KEYBOARD

cog = Blueprint("Entertainment")
cog.labeler.vbml_ignore_case = True

@cog.on.message(text=["развлечения", "😄 развлечения"])
async def entertainment(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.action == "main" and player.keyb == 1:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], это отдел развлечений:
			Казино - разные виды игр для поднятия ресурсов 🎰
			Путешествия""", keyboard=entkeyb)
		Player.set_action(player.uid, "ent")
		print(f"{player.nickname} [{player.uid}] called 'entertainment'")
	if player != False and player.action == "main" and player.keyb == 0:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], это отдел развлечений:
			Казино - разные виды игр для поднятия ресурсов 🎰
			Путешествия""", keyboard=EMPTY_KEYBOARD)
		Player.set_action(player.uid, "ent")
		print(f"{player.nickname} [{player.uid}] called 'entertainment'")

@cog.on.message(text=["казино"])
async def casino(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.action == "ent" and player.keyb == 1:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], это отдел казино 🎰:
			Блек Джек
			(скоро)""", keyboard=casinokeyb)
		Player.set_action(player.uid, "casino")
		print(f"{player.nickname} [{player.uid}] called 'casino'")
	if player != False and player.action == "ent" and player.keyb == 0:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], это отдел казино 🎰:
			Блек Джек
			(скоро)""", keyboard=EMPTY_KEYBOARD)
		Player.set_action(player.uid, "casino")
		print(f"{player.nickname} [{player.uid}] called 'casino'")