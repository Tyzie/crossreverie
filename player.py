import psycopg2 as ps
from config import DB_URI
import random
from datetime import date
import random

class Player():
    def __init__(self, id, uid, ban, nickname, race, health, maxhealth, level, xp, maxxp, gold, silver, copper, dater, donate, manna, maxmanna):
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
            cur.execute("INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (id, ids[0], "false", nick, racer, 250, 250, 1, 0, 8, 0, 0, 0, daterr, "Нет", 0, 1000))
        if racer == "Демон":
            cur.execute("INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (id, ids[0], "false", nick, racer, 1000, 1000, 1, 0, 8, 0, 0, 0, daterr, "Нет", 0, 1000))
        if racer == "Ангел":
            cur.execute("INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (id, ids[0], "false", nick, racer, 750, 750, 1, 0, 8, 0, 0, 0, daterr, "Нет", 0, 1000))
        if racer == "Эльф":
            cur.execute("INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (id, ids[0], "false", nick, racer, 500, 500, 1, 0, 8, 0, 0, 0, daterr, "Нет", 0, 1000))
        cur.execute("UPDATE ids SET uids=uids+1")
        db.commit()
        return racer

    @staticmethod
    def get_profile(id):
        db = ps.connect(DB_URI, sslmode="require")
        cur = db.cursor()
        cur.execute(f"SELECT * FROM users WHERE id='{id}'")
        i = cur.fetchone()
        if i == None:
            return False
        if i != None:
            return Player(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16])