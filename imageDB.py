import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS dropTable (id INTEGER PRIMARY KEY AUTOINCREMENT, str TEXT, notes TEXT, image BLOB)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM dropTable")
        rows = self.cur.fetchall()
        return rows

    def fetchOne(self, id):
        self.cur.execute("SELECT image FROM dropTable WHERE id=?", (id,))
        rows = self.cur.fetchall()[0][0]
        return rows

    def insert(self, str, notes, image):
        self.cur.execute("INSERT INTO dropTable VALUES (NULL, ?, ?, ?)",
                         (str, notes, image))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM dropTable WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, str, notes, image):
        self.cur.execute(
            "UPDATE dropTable SET str = ?, notes = ?, image =? WHERE id = ?", (str, notes, image, id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


db = Database('imageDB.db')
