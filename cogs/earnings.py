from vkbottle.bot import Blueprint, Message
from player import Player
from config import mainkeyb, earnkeyb, convkeyb, jobskeyb, choicekeyb, EMPTY_KEYBOARD
import asyncio

cog = Blueprint("Earnings")
cog.labeler.vbml_ignore_case = True

@cog.on.message(text=["заработок", "💼 заработок"])
async def earnings(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.action == "main" and player.keyb == 1:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], тебе доступны данные способы заработка:
			Обменник валют - здесь ты можешь обменять нужную тебе валюту на другую ⭐
			Работы - здесь есть вакансии для того, что получить немного ресурсов!""", keyboard=earnkeyb)
		Player.set_action(player.uid, "earn")
		print(f"{player.nickname} [{player.uid}] called 'earnings'")
	if player != False and player.action == "main" and player.keyb == 0:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], тебе доступны данные способы заработка:
			Обменник валют - здесь ты можешь обменять нужную тебе валюту на другую ⭐
			Работы - здесь есть вакансии для того, что получить немного ресурсов!""", keyboard=EMPTY_KEYBOARD)
		Player.set_action(player.uid, "earn")
		print(f"{player.nickname} [{player.uid}] called 'earnings'")

#@cog.on.message(text=["обменник валют"])
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

@cog.on.message(text=["работы"])
async def jobs(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.action == "earn" and player.keyb == 1:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], здесь ты можешь подобрать себе работу:
			=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
			Уборщик | Время: 5 секунд ⌚ | Медь: 1-3 🟧 | Опыт: 0-1 ⭐
			Продавец | Время: 10 секунд ⌚ | Медь: 1-5 🟧 | Опыт 0-2 ⭐""", keyboard=jobskeyb)
		Player.set_action(player.uid, "jobs")
		print(f"{player.nickname} [{player.uid}] called 'jobs'")
	if player != False and player.action == "earn" and player.keyb == 0:
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], здесь ты можешь подобрать себе работу:
			=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
			Уборщик | Время: 5 секунд ⌚ | Медь: 1-3 🟧 | Опыт: 0-1 ⭐
			Продавец | Время: 10 секунд ⌚ | Медь: 1-5 🟧 | Опыт 0-2 ⭐""", keyboard=EMPTY_KEYBOARD)
		Player.set_action(player.uid, "jobs")
		print(f"{player.nickname} [{player.uid}] called 'jobs'")

@cog.on.message(text=["уборщик"])
async def cleaner(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.action == "jobs" and player.keyb == 1:
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], взял в руки метлу 🧹")
		await asyncio.sleep(1)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], начал подметать комнату 🧹")
		await asyncio.sleep(4)
		i = Player.job(player.uid, 1)
		Player.set_action(player.uid, "cleaner")
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], получил: 
			| Опыт: +{i[0]} ⭐
			| Медь: +{i[1]} 🟧 
			Продолжить?""", keyboard=choicekeyb)
	if player != False and player.action == "jobs" and player.keyb == 0:
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], взял в руки метлу 🧹")
		await asyncio.sleep(1)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], начал подметать комнату 🧹🍃")
		await asyncio.sleep(4)
		i = Player.job(player.uid, 1)
		Player.set_action(player.uid, "cleaner")
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}], получил: 
			| Опыт: +{i[0]} ⭐
			| Медь: +{i[1]} 🟧 
			Продолжить?""", keyboard=EMPTY_KEYBOARD)

@cog.on.message(text=["продавец"])
async def salesman(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.action == "jobs" and player.keyb == 1:
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], встал на рабочее место 🏪")
		await asyncio.sleep(5)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], пробил продукты 🍉")
		await asyncio.sleep(2)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], принял оплату 💰")
		await asyncio.sleep(3)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], отдал сдачу 💵")
		i = Player.job(player.uid, 2)
		Player.set_action(player.uid, "salesman")
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}] получил: 
			| Опыт: +{i[0]} ⭐
			| Медь: +{i[1]} 🟧 
			Продолжить?""", keyboard=choicekeyb)
	if player != False and player.action == "jobs" and player.keyb == 0:
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], встал на рабочее место 🏪")
		await asyncio.sleep(5)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], пробил продукты 🍉")
		await asyncio.sleep(2)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], принял оплату 💰")
		await asyncio.sleep(3)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], отдал сдачу 💵")
		i = Player.job(player.uid, 2)
		Player.set_action(player.uid, "salesman")
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}] получил: 
			| Опыт: +{i[0]} ⭐
			| Медь: +{i[1]} 🟧 
			Продолжить?""", keyboard=EMPTY_KEYBOARD)

@cog.on.message(text=["да"])
async def choice_yes(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.action == "cleaner" and player.keyb == 1:
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}] взял в руки метлу 🧹")
		await asyncio.sleep(1)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}] начал подметать комнату 🧹")
		await asyncio.sleep(4)
		i = Player.job(player.uid, 1)
		Player.set_action(player.uid, "cleaner")
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}] получил: 
			| Опыт: +{i[0]} ⭐
			| Медь: +{i[1]} 🟧 
			Продолжить?""", keyboard=choicekeyb)
	if player != False and player.action == "cleaner" and player.keyb == 0:
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}] взял в руки метлу 🧹")
		await asyncio.sleep(1)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}] начал подметать комнату 🧹")
		await asyncio.sleep(4)
		i = Player.job(player.uid, 1)
		Player.set_action(player.uid, "cleaner")
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}] получил: 
			| Опыт: +{i[0]} ⭐
			| Медь: +{i[1]} 🟧 
			Продолжить?""", keyboard=EMPTY_KEYBOARD)
	if player != False and player.action == "salesman" and player.keyb == 1:
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], встал на рабочее место 🏪")
		await asyncio.sleep(5)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], пробил продукты 🍉")
		await asyncio.sleep(2)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], принял оплату 💰")
		await asyncio.sleep(3)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], отдал сдачу 💵")
		i = Player.job(player.uid, 2)
		Player.set_action(player.uid, "salesman")
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}] получил: 
			| Опыт: +{i[0]} ⭐
			| Медь: +{i[1]} 🟧 
			Продолжить?""", keyboard=choicekeyb)
	if player != False and player.action == "salesman" and player.keyb == 0:
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], встал на рабочее место 🏪")
		await asyncio.sleep(5)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], пробил продукты 🍉")
		await asyncio.sleep(2)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], принял оплату 💰")
		await asyncio.sleep(3)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], отдал сдачу 💵")
		i = Player.job(player.uid, 2)
		Player.set_action(player.uid, "salesman")
		await message.answer(f"""[id{player.id}|{player.nickname}] [{player.uid}] получил: 
			| Опыт: +{i[0]} ⭐
			| Медь: +{i[1]} 🟧 
			Продолжить?""", keyboard=EMPTY_KEYBOARD)

@cog.on.message(text=["нет"])
async def choice_no(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.action == "cleaner" and player.keyb == 1:
		Player.set_action(player.uid, "main")
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], приходи еще, работа всегда найдется!", keyboard=mainkeyb)
	if player != False and player.action == "cleaner" and player.keyb == 0:
		Player.set_action(player.uid, "main")
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], приходи еще, работа всегда найдется!", keyboard=EMPTY_KEYBOARD)
	if player != False and player.action == "salesman" and player.keyb == 1:
		Player.set_action(player.uid, "main")
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], приходи еще, работа всегда найдется!", keyboard=mainkeyb)
	if player != False and player.action == "salesman" and player.keyb == 0:
		Player.set_action(player.uid, "main")
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], приходи еще, работа всегда найдется!", keyboard=EMPTY_KEYBOARD)

#@cog.on.message(text="<numb>")
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
