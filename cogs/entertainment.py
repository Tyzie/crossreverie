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
			Казино - обычное казино для поднятия ресурсов 🔥
			Путешествия""", keyboard=entkeyb)
		Player.set_action(player.uid, "ent")
		print(f"{player.nickname} [{player.uid}] called 'entertainment'")
	if player != False and player.action == "main" and player.keyb == 0:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], это отдел развлечений:
			Казино - обычное казино для поднятия ресурсов 🔥
			Путешествия""", keyboard=EMPTY_KEYBOARD)
		Player.set_action(player.uid, "ent")
		print(f"{player.nickname} [{player.uid}] called 'entertainment'")

@cog.on.message(text=["казино"])
async def casino(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.action == "ent" and player.keyb == 1:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], это казино 🎰:
			=-=-=-=-=-=-=-=-=-=-=-=-=
			Выбери валюту для игры:
			🟧 Медь""", keyboard=casinokeyb)
		Player.set_action(player.uid, "casino")
		print(f"{player.nickname} [{player.uid}] called 'casino'")
	if player != False and player.action == "ent" and player.keyb == 0:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], это казино 🎰:
			=-=-=-=-=-=-=-=-=-=-=-=-=
			Выбери валюту для игры:
			🟧 Медь""", keyboard=EMPTY_KEYBOARD)
		Player.set_action(player.uid, "casino")
		print(f"{player.nickname} [{player.uid}] called 'casino'")

@cog.on.message(text=["🟧", "🟧 медь", "медь"])
async def copper_casino(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.action == "casino":
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], введи свою ставку 🎰")
		Player.set_action(player.uid, "copper_casino")
		print(f"{player.nickname} [{player.uid}] called 'copper_casino'")

@cog.on.message(text=['<numb>'])
async def copper_casino_numb(message: Message, numb=None):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.action == "copper_casino" and player.keyb == 1:
		i = Player.casino(player.uid, 1, numb)
		if i == 0:
			await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], ты проиграл {numb} меди 🟧! ❌", keyboard=mainkeyb)
			Player.set_action(player.uid, "main")
			print(f"{player.nickname} [{player.uid}] called 'copper_casino_numb' numb: {numb}")
		if i == 1:
			await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], ты победил и получил {numb} меди 🟧! ✔", keyboard=mainkeyb)
			Player.set_action(player.uid, "main")
			print(f"{player.nickname} [{player.uid}] called 'copper_casino_numb' numb: {numb}")
	if player != False and player.action == "copper_casino" and player.keyb == 0:
		i = Player.casino(player.uid, 1, numb)
		if i == 0:
			await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], ты проиграл {numb} меди 🟧! ❌", keyboard=EMPTY_KEYBOARD)
			Player.set_action(player.uid, "main")
			print(f"{player.nickname} [{player.uid}] called 'copper_casino_numb' numb: {numb}")
		if i == 1:
			await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], ты победил и получил {numb} меди 🟧! ✔", keyboard=EMPTY_KEYBOARD)
			Player.set_action(player.uid, "main")
			print(f"{player.nickname} [{player.uid}] called 'copper_casino_numb' numb: {numb}")