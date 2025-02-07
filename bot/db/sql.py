import sqlite3

class DataBase:
    def __init__(self):
        self.dbname = 'bot.db'
        self.conn = sqlite3.connect(self.dbname)
        self._set_up()

    def _set_up(self):
        cur = self.conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS Guilds(id INTEGER, server_id STRING, max_pitch INTEGER, max_second INTEGER)')
        self.conn.commit()

    def exec_query(self,query:str):
        cur = self.conn.cursor()
        cur.execute(query)
        for x in cur.fetchall():
            print(x)

    def close(self):
        self.conn.close()