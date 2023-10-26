import sqlite3
from datetime import datetime

class TimeTracker:
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

    def record_time(self, date, start_time, end_time, task, tag):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO time_records (date, start_time, end_time, task, tag) VALUES (?, ?, ?, ?, ?)",
                       (date, start_time, end_time, task, tag))
        self.conn.commit()

    def query_time(self, date=None, task=None, tag=None):
        cursor = self.conn.cursor()
        query = "SELECT * FROM time_records WHERE 1"
        if date:
            query += f" AND date = '{date}'"
        if task:
            query += f" AND task LIKE '%{task}%'"
        if tag:
            query += f" AND tag = '{tag}'"

        cursor.execute(query)
        records = cursor.fetchall()
        return records

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    tracker = TimeTracker("time_tracker.db")

    while True:
        print("\nOptions:")
        print("1. Record time")
        print("2. Query time")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            date = input("Date (YYYY/MM/DD or today): ")
            if date == "today":
                date = datetime.now().strftime("%Y/%m/%d")
            start_time = input("Start time (HH:MM AM/PM): ")
            end_time = input("End time (HH:MM AM/PM): ")
            task = input("Task: ")
            tag = input("Tag: ")
            tracker.record_time(date, start_time, end_time, task, tag)
            print("Time recorded successfully!")

        elif choice == "2":
            date = input("Date (YYYY/MM/DD) or press Enter to query all: ")
            task = input("Task (press Enter to skip): ")
            tag = input("Tag (press Enter to skip): ")
            records = tracker.query_time(date, task, tag)
            print("\nQuery results:")
            for record in records:
                print(f"{record[1]} {record[2]} - {record[3]}: {record[4]} ({record[5]})")

        elif choice == "3":
            tracker.close()
            break
