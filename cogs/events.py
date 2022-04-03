from vkbottle.bot import Blueprint, Message
from vkbottle import GroupTypes, GroupEventType
import psycopg2 as ps
from player import Player
from config import DB_URI, mainkeyb, EMPTY_KEYBOARD

cog = Blueprint("Events")
cog.labeler.vbml_ignore_case = True

@cog.on.raw_event(GroupEventType.GROUP_JOIN, dataclass=GroupTypes.GroupJoin)
async def group_join_handler(event: GroupTypes.GroupJoin):
    user = await cog.api.users.get(event.object.user_id)
    db = ps.connect(DB_URI)
    cur = db.cursor()
    cur.execute(f"SELECT id FROM users WHERE id={user[0].id}")
    check = cur.fetchone()
    cur.execute(f"SELECT id FROM sub WHERE id={user[0].id}")
    check2 = cur.fetchone()
    if check != None and check2 == None:
        await cog.api.messages.send(
            peer_id=event.object.user_id,
            message=f"""🔥 Спасибо, что вступил в наше сообщество, [id{user[0].id}|{user[0].first_name}]
        За это ты получаешь 250 🟧 на свой аккаунт!!! ⭐""",
            random_id=0,
            keyboard=mainkeyb
        )
        cur.execute(f"UPDATE users SET copper=copper+250 WHERE id={user[0].id}")
        cur.execute(f"INSERT INTO sub VALUES('{user[0].id}')")
        db.commit()
    if check != None and check2 != None:
        await cog.api.messages.send(
            peer_id=event.object.user_id,
            message=f"""🔥 Спасибо, что снова вступил в наше сообщество, [id{user[0].id}|{user[0].first_name}]""",
            random_id=0,
            keyboard=mainkeyb
        )
    if check == None:
        pass

@cog.on.raw_event(GroupEventType.GROUP_LEAVE, dataclass=GroupTypes.GroupLeave)
async def group_leave_handler(event: GroupTypes.GroupLeave):
    user = await cog.api.users.get(event.object.user_id)
    await cog.api.messages.send(
        peer_id=event.object.user_id,
        message=f"""Жалко, что ты ушел от нас, [id{user[0].id}|{user[0].first_name}] 😢""",
        random_id=0,
        keyboard=mainkeyb
    )