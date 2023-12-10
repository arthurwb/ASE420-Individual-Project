import sqlite3

class DatabaseManager:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS time_records (
                        id INTEGER PRIMARY KEY,
                        date DATE,
                        start_time TIME,
                        end_time TIME,
                        task TEXT,
                        tag TEXT)''')
        self.conn.commit()

    def close(self):
        self.conn.close()