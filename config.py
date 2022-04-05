from vkbottle import Keyboard, KeyboardButtonColor, Text, EMPTY_KEYBOARD

DB_URI = "postgres://zixigujjprjyih:1a1bf09ccde0e5eba271a5b48e0dfeb04e63f8ec03fe3c85cb394350224a2933@ec2-52-18-116-67.eu-west-1.compute.amazonaws.com:5432/dtr3j3emc4bvt"
token = "e455d14cca6615a47f3a23e185776230a820ea79b7320ccc444ed95385941b5450d94504122a8adcd6b6d"

mainkeyb = (
    Keyboard(one_time=False, inline=False)
    .add(Text("👤 Профиль"), color=KeyboardButtonColor.SECONDARY)
    .add(Text("Магазин"), color=KeyboardButtonColor.NEGATIVE)
    .add(Text("💼 Заработок"), color=KeyboardButtonColor.SECONDARY)
    .add(Text("Магия"), color=KeyboardButtonColor.NEGATIVE)
    .row()
    .add(Text("Имущество"), color=KeyboardButtonColor.NEGATIVE)
    .add(Text("Бизнес"), color=KeyboardButtonColor.NEGATIVE)
    .add(Text("😄 Развлечения"), color=KeyboardButtonColor.SECONDARY)
    .add(Text("Карта"), color=KeyboardButtonColor.NEGATIVE)
    .row()
    .add(Text("🎒"), color=KeyboardButtonColor.NEGATIVE)
    .add(Text("Топ"), color=KeyboardButtonColor.NEGATIVE)
    .add(Text("📜 Помощь"), color=KeyboardButtonColor.PRIMARY)
    .add(Text("⚙"), color=KeyboardButtonColor.PRIMARY)
    .get_json()
)

setkeyb = (
    Keyboard(inline=True)
    .add(Text("Клавиатура вкл"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("Клавиатура выкл"), color=KeyboardButtonColor.NEGATIVE)
    .get_json()
)

earnkeyb = (
    Keyboard(one_time=True, inline=False)
    .add(Text("Работы"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("Биржа"), color=KeyboardButtonColor.NEGATIVE)
    .row()
    .add(Text("Обменник валют"), color=KeyboardButtonColor.PRIMARY)
    .add(Text("Рабы"), color=KeyboardButtonColor.NEGATIVE)
    .get_json()
)
convkeyb = (
    Keyboard(inline=True)
    .add(Text("🟧 в ⬜"), color=KeyboardButtonColor.POSITIVE)
    .get_json()
)
jobskeyb = (
    Keyboard(inline=True)
    .add(Text("Уборщик"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("Продавец"), color=KeyboardButtonColor.POSITIVE)
    .get_json()
    )
choicekeyb = (
    Keyboard(inline=True)
    .add(Text("Да"), color=KeyboardButtonColor.POSITIVE)
    .add(Text("Нет"), color=KeyboardButtonColor.NEGATIVE)
    .get_json()
    )

entkeyb = (
    Keyboard(inline=True)
    .add(Text("Казино"), color=KeyboardButtonColor.NEGATIVE)
    .add(Text("Путешествия"), color=KeyboardButtonColor.NEGATIVE)
    .get_json()
    )

