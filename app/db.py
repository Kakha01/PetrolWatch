import sqlite3
import os
from flask import g, current_app

basedir = os.path.abspath(os.path.dirname(__file__))


def connect_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db():
    db: sqlite3.Connection = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    db = connect_db()

    with open(os.path.join(basedir, "schema.sql")) as f:
        cur = db.cursor()

        cur.execute(f.read())

        db.commit()
