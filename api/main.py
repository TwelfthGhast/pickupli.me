import os
import sqlite3

from fastapi import FastAPI

app = FastAPI()

cur_path = os.path.dirname(os.path.realpath(__file__))

SOURCE_DB = sqlite3.connect("pickuplime.db")
with open(f"{cur_path}/init.sql", "r") as fp:
    cur = SOURCE_DB.cursor()
    schema = fp.read()
    cur.executescript(schema)
    cur.close()
MEM_DB = sqlite3.connect(":memory:")
SOURCE_DB.backup(MEM_DB)
SOURCE_DB.close()


@app.get("/pickuplime")
async def get_lime():
    cur = MEM_DB.cursor()
    cur.execute("SELECT pickuplime FROM pickuplimes LIMIT 1")
    lime, = cur.fetchone()
    cur.close()
    return {"lime": lime}
