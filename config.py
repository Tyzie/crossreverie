from vkbottle import Keyboard, KeyboardButtonColor, Text

DB_URI = "postgres://zixigujjprjyih:1a1bf09ccde0e5eba271a5b48e0dfeb04e63f8ec03fe3c85cb394350224a2933@ec2-52-18-116-67.eu-west-1.compute.amazonaws.com:5432/dtr3j3emc4bvt"
token = "e455d14cca6615a47f3a23e185776230a820ea79b7320ccc444ed95385941b5450d94504122a8adcd6b6d"

mainkeyb = (
    Keyboard(one_time=False, inline=False)
    .add(Text("Профиль"), color=KeyboardButtonColor.SECONDARY)
    .add(Text("Магазин"), color=KeyboardButtonColor.SECONDARY)
    .add(Text("Работа"), color=KeyboardButtonColor.SECONDARY)
    .add(Text("Магия"), color=KeyboardButtonColor.SECONDARY)
    .row()
    .add(Text("Имущество"), color=KeyboardButtonColor.SECONDARY)
    .add(Text("Бизнес"), color=KeyboardButtonColor.SECONDARY)
    .add(Text("Казино"), color=KeyboardButtonColor.SECONDARY)
    .add(Text("Карта"), color=KeyboardButtonColor.SECONDARY)
    .row()
    .add(Text("🎒"), color=KeyboardButtonColor.PRIMARY)
    .add(Text("Топ"), color=KeyboardButtonColor.PRIMARY)
    .add(Text("Помощь"), color=KeyboardButtonColor.PRIMARY)
    .add(Text("⚙"), color=KeyboardButtonColor.PRIMARY)
    .get_json()
)

