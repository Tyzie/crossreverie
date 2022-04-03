from vkbottle.bot import Blueprint, Message
from player import Player
from config import mainkeyb, earnkeyb, convkeyb, EMPTY_KEYBOARD

cog = Blueprint("Earnings")
cog.labeler.vbml_ignore_case = True

@cog.on.message(text=["заработок"])
async def earnings(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.action == "main" and player.keyb == 1:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], тебе доступны данные способы заработка:
			Обменник валют - здесь ты можешь обменять нужную тебе валюту на другую""", keyboard=earnkeyb)
		Player.set_action(player.uid, "earn")
		print(f"{player.nickname} [{player.uid}] called 'earnings'")
	if player != False and player.action == "main" and player.keyb == 0:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], тебе доступны данные способы заработка:
			Обменник валют - здесь ты можешь обменять нужную тебе валюту на другую ⭐""", keyboard=EMPTY_KEYBOARD)
		Player.set_action(player.uid, "earn")
		print(f"{player.nickname} [{player.uid}] called 'earnings'")

@cog.on.message(text=["обменник валют"])
async def converter(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.action == "earn" and player.keyb == 1:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], это обменник валют:
			Обменник валют - здесь ты можешь обменять нужную тебе валюту на другую
			-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
			1 ⬜ = 100 🟧
			-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
			Доступные команды:
			🟧 в ⬜
			""", keyboard=convkeyb)
		Player.set_action(player.uid, "conv")
		print(f"{player.nickname} [{player.uid}] called 'converter'")
	if player != False and player.action == "earn" and player.keyb == 0:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], это обменник валют:
			Обменник валют - здесь ты можешь обменять нужную тебе валюту на другую
			-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
			1 ⬜ = 100 🟧
			-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
			Доступные команды:
			🟧 в ⬜
			""", keyboard=EMPTY_KEYBOARD)
		Player.set_action(player.uid, "conv")
		print(f"{player.nickname} [{player.uid}] called 'converter'")

@cog.on.message(text=["🟧 в ⬜"])
async def bronze_silver(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.action == "conv" and player.keyb == 1:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], укажи сколько ты хочешь обменять:""", keyboard=mainkeyb)
		Player.set_action(player.uid, "bronze_silver")
		print(f"{player.nickname} [{player.uid}] called 'bronze_silver'")
	if player != False and player.action == "conv" and player.keyb == 0:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], укажи сколько ты хочешь обменять:""", keyboard=EMPTY_KEYBOARD)
		Player.set_action(player.uid, "bronze_silver")
		print(f"{player.nickname} [{player.uid}] called 'bronze_silver'")

@cog.on.message(text="<numb>")
async def conv(message: Message, numb=None):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.action == "bronze_silver" and player.keyb == 1:
		i = Player.bronze_silver(player.uid, numb)
		if i != False:
			await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], ты обменял {numb} 🟧 в серебро ⬜!", keyboard=mainkeyb)
		if i == False:
			await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], тебе нехватает меди 🟧 для обмена! ❌", keyboard=mainkeyb)
		Player.set_action(player.uid, "main")
		print(f"{player.nickname} [{player.uid}] called 'conv_bs' numb: {numb}")
	if player != False and player.action == "bronze_silver" and player.keyb == 0:
		i = Player.bronze_silver(player.uid, numb)
		if i != False:
			await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], ты обменял {numb} 🟧 в серебро ⬜!", keyboard=EMPTY_KEYBOARD)
		if i == False:
			await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], тебе нехватает меди 🟧 для обмена! ❌", keyboard=EMPTY_KEYBOARD)
		Player.set_action(player.uid, "main")
		print(f"{player.nickname} [{player.uid}] called 'conv_bs' numb: {numb}")
