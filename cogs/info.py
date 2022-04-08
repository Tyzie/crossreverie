from vkbottle.bot import Blueprint, Message
from player import Player
from config import mainkeyb, EMPTY_KEYBOARD

cog = Blueprint("Information")
cog.labeler.vbml_ignore_case = True

@cog.on.message(text=["информация", "🔰 информация"])
async def info(message: Message):
	user = await cog.api.users.get(message.from_id)
	player = Player.get_profile(user[0].id)
	if player != False and player.keyb == 1:
		await message.answer(f"""Информация о боте, [id{player.id}|{player.nickname}] [{player.uid}]
Данный бот "Cross Reverie" - обычный игровой бот для ВК 👤. Здесь ты можешь прокачивать персонажа,
скупать магазин, развлекаться в казино и уничтожать врагов! 🔥
У бота есть поддержка коммьюнити и разработчиков, поэтому бот сейчас активно живет и развивается! 💚
Если комьюнити бота будет постоянно активное и доброжелательное, разработчики буду быстрее выпускать обновы и промокоды. ✔
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
С уважением, [id577675287|Создатель] и [id442819858|Кодер(разработчик)] ❤""", keyboard=mainkeyb)
		Player.set_action(player.uid, "main")
		print(f"{player.nickname} [{player.uid}] called 'info'")
	if player != False and player.keyb == 0:
		await message.answer(f"""Информация о боте, [id{player.id}|{player.nickname}] [{player.uid}]
Данный бот "Cross Reverie" - обычный игровой бот для ВК 👤. Здесь ты можешь прокачивать персонажа,
скупать магазин, развлекаться в казино и уничтожать врагов! 🔥
У бота есть поддержка коммьюнити и разработчиков, поэтому бот сейчас активно живет и развивается! 💚
Если комьюнити бота будет постоянно активное и доброжелательное, разработчики буду быстрее выпускать обновы и промокоды. ✔
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
С уважением, [id577675287|Создатель] и [id442819858|Кодер(разработчик)] ❤""", keyboard=EMPTY_KEYBOARD)
		Player.set_action(player.uid, "main")
		print(f"{player.nickname} [{player.uid}] called 'info'")