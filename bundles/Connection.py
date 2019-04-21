import sqlite3
from db_config import *
from flask import g

class Connection():

    def __init__(self):
        pass

    def execute(self, query, args):
        db = self.get_db()
        cur = db.cursor()
        cur.execute(query, args)
        db.commit()

    def get_db(self):
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)
        return db

    def query_db(self, query, args=(), one=False):
        cur = self.get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

    def init_db(self, app):
        with app.app_context():
            db = self.get_db()
            with app.open_resource('schema.sql', mode='r') as f:
                db.cursor().executescript(f.read())
            db.commit()

    def maybe_close_db(self):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()
