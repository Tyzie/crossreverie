from vkbottle.bot import Blueprint, Message
from player import Player
from config import mainkeyb, setkeyb, EMPTY_KEYBOARD

cog = Blueprint("Settings")
cog.labeler.vbml_ignore_case = True

@cog.on.message(text=["⚙", "настройки", "⚙ настройки"])
async def earnings(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False:
		await message.answer(f"""Настройки бота, [id{player.id}|{player.nickname}] [{player.uid}]
			-=-=-=-=-=-=-=-=-=-=-
			Клавиатуру можно включить командой "Клавиатура вкл"✔
			Клавиатуру можно выключить командой "Клавиатура выкл"❌
			-=-=-=-=-=-=-=-=-=-=-
			Игровой никнейм можно поменять командой "ник [новый ник]" 💬""", keyboard=setkeyb)

@cog.on.message(text=["клавиатура вкл"])
async def keyb_on(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False:
		Player.keyb(player.uid, 1)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], ты включил клавиатуру в боте! ✔", keyboard=mainkeyb)

@cog.on.message(text=["клавиатура выкл"])
async def keyb_on(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False:
		Player.keyb(player.uid, 0)
		await message.answer(f"[id{player.id}|{player.nickname}] [{player.uid}], ты выключил клавиатуру в боте! ❌", keyboard=EMPTY_KEYBOARD)
