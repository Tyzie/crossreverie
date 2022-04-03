import psycopg2 as ps
from config import DB_URI
import random
from datetime import date
import random
import asyncio

class Player():
    def __init__(self, id, uid, ban, nickname, race, health, maxhealth, level, xp, maxxp, gold, silver, copper, dater, donate, manna, maxmanna, action, keyb):
        self.id = id
        self.uid = uid
        self.ban = ban
        self.nickname = nickname
        self.race = race
        self.health = health
        self.maxhealth = maxhealth
        self.level = level
        self.xp = xp
        self.maxxp = maxxp
        self.gold = gold
        self.silver = silver
        self.copper = copper
        self.dater = dater
        self.donate = donate
        self.manna  = manna
        self.maxmanna = maxmanna
        self.action = action
        self.keyb = keyb

    @staticmethod
    def create_profile(id, nick):
        db = ps.connect(DB_URI, sslmode="require")
        cur = db.cursor()
        cur.execute("SELECT uids FROM ids")
        ids = cur.fetchone()
        x = random.randint(0, 10)
        if x == 3:
            racer = "Демон"
        if x == 6:
            racer = "Эльф"
        if x == 9:
            racer = "Ангел"
        else:
            racer = "Человек"
        daterr = date.today()
        if racer == "Человек":
            cur.execute("INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (id, ids[0], "false", nick, racer, 250, 250, 1, 0, 8, 0, 0, 0, daterr, "Нет", 0, 1000, "main", 1))
        if racer == "Демон":
            cur.execute("INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (id, ids[0], "false", nick, racer, 1000, 1000, 1, 0, 8, 0, 0, 0, daterr, "Нет", 0, 1000, "main", 1))
        if racer == "Ангел":
            cur.execute("INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (id, ids[0], "false", nick, racer, 750, 750, 1, 0, 8, 0, 0, 0, daterr, "Нет", 0, 1000, "main", 1))
        if racer == "Эльф":
            cur.execute("INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (id, ids[0], "false", nick, racer, 500, 500, 1, 0, 8, 0, 0, 0, daterr, "Нет", 0, 1000, "main", 1))
        cur.execute("UPDATE ids SET uids=uids+1")
        db.commit()
        return racer

    @staticmethod
    def get_profile(id):
        db = ps.connect(DB_URI, sslmode="require")
        cur = db.cursor()
        cur.execute(f"SELECT gold, silver, copper, xp, maxxp, health, maxhealth FROM users WHERE id='{id}'")
        g = cur.fetchone()
        s = round(g[1], 1)
        cur.execute(f"UPDATE users SET silver='{s}' WHERE id='{id}'")
        db.commit()
        cur.execute(f"SELECT * FROM users WHERE id='{id}'")
        i = cur.fetchone()
        if i == None:
            return False
        if i != None:
            return Player(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18])

    def set_action(id, act):
        db = ps.connect(DB_URI, sslmode="require")
        cur = db.cursor()
        cur.execute(f"UPDATE users SET action='{act}' WHERE uid='{id}'")
        db.commit()

    def keyb(id, ke):
        db = ps.connect(DB_URI, sslmode="require")
        cur = db.cursor()
        cur.execute(f"UPDATE users SET keyb='{ke}' WHERE uid='{id}'")
        db.commit()

    def set_nick(id, nick):
        db = ps.connect(DB_URI, sslmode="require")
        cur = db.cursor()
        cur.execute(f"UPDATE users SET nickname='{nick}' WHERE uid='{id}'")
        db.commit()

    def bronze_silver(id, numb):
        db = ps.connect(DB_URI, sslmode="require")
        cur = db.cursor()
        cur.execute(f"SELECT copper FROM users WHERE uid='{id}'")
        i = cur.fetchone()
        if i[0] >= float(numb):
            x = float(numb)/100
            cur.execute(f"UPDATE users SET silver=silver+'{d}' WHERE uid='{id}'")
            cur.execute(f"UPDATE users SET copper=copper-'{numb}' WHERE uid='{id}'")
            db.commit()
        if i[0] < float(numb):
            return False

    def job(id, jid):
        db = ps.connect(DB_URI, sslmode="require")
        cur = db.cursor()
        if jid == 1:
            x = random.randint(0,1)
            m = random.randint(1,3)
            cur.execute(f"UPDATE users SET xp=xp+'{x}' WHERE uid='{id}'")
            cur.execute(f"UPDATE users SET copper=copper+'{m}' WHERE uid='{id}'")
            db.commit()
            return x, m