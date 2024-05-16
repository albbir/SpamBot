import sqlite3

class SpamDB:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def get_spam(self):
        self.cursor.execute("SELECT name, count FROM SPA")
        result = self.cursor.fetchall()
        return result
    def close(self):
        self.conn.close()