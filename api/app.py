import sqlite3

from fastapi import FastAPI

app = FastAPI()

SOURCE_DB = sqlite3.connect("pickuplime.db")
with open("init.sql", "r") as fp:
    cur = SOURCE_DB.cursor()
    schema = fp.read()
    cur.executescript(schema)
    cur.close()
MEM_DB = sqlite3.connect(":memory:")
SOURCE_DB.backup(MEM_DB)
SOURCE_DB.close()
