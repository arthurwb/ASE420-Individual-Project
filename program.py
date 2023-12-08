import sqlite3
from datetime import datetime
from collections import Counter
from dateutil import parser

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

class TimeTracker:
    def __init__(self, database_name):
        self.db_manager = DatabaseManager(database_name)

    def record_time(self, date, start_time, end_time, task, tag):
        if not date or not start_time or not end_time or not task or not tag:
            raise ValueError("Error: Please provide values for all fields.")

        cursor = self.db_manager.conn.cursor()
        cursor.execute("INSERT INTO time_records (date, start_time, end_time, task, tag) VALUES (?, ?, ?, ?, ?)",
                       (date, start_time, end_time, task, tag))
        self.db_manager.conn.commit()
        print("Time recorded successfully!")

    def construct_query(self, start_date, end_date, task, tag):
        query = "SELECT * FROM time_records WHERE 1"

        if start_date and end_date:
            query += f" AND date BETWEEN '{start_date}' AND '{end_date}'"
        elif start_date:
            query += f" AND date >= '{start_date}'"
        elif end_date:
            query += f" AND date <= '{end_date}'"

        if task:
            query += f" AND task LIKE '%{task}%'"
        if tag:
            query += f" AND tag = '{tag}'"

        return query

    def query_time(self, start_date=None, end_date=None, task=None, tag=None):
        cursor = self.db_manager.conn.cursor()
        query = self.construct_query(start_date, end_date, task, tag)
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    def generate_report(self, start_date, end_date):
        records = self.query_time(start_date=start_date, end_date=end_date)
        report = f"\nTime Usage Report ({start_date} to {end_date}):\n"
        for record in records:
            report += f"{record[1]} {record[2]} - {record[3]}: {record[4]} ({record[5]})\n"
        return report

    def priority_command(self, num_activities=5):
        all_records = self.query_time()
        tag_times = Counter(record[5] for record in all_records)
        most_common_tasks = tag_times.most_common(num_activities)

        result = f"\nActivities with the highest time spent:\n"
        for tag, count in most_common_tasks:
            result += f"{tag}: {count} occurrences\n"
        return result

    def close(self):
        self.db_manager.close()

if __name__ == "__main__":
    tracker = TimeTracker("time_tracker.db")

    while True:
        print("\nOptions:")
        print("1: Record time")
        print("2: Query time")
        print("3: Generate Time Usage Report")
        print("4: Activities with Highest Time Spent (Priority Command)")
        print("q: Exit")
        choice = input("Enter your choice (1/2/3/4/q): ")

        if choice == "1":
            date = input("Date (YYYY/MM/DD or today): ")
            if date == "today":
                date = parser.parse("today").strftime("%Y/%m/%d")
            start_time = input("Start time (HH:MM AM/PM): ")
            end_time = input("End time (HH:MM AM/PM): ")
            task = input("Task: ")
            tag = input("Tag: ")

            tracker.record_time(date, start_time, end_time, task, tag)

        elif choice == "2":
            date = input("Date (YYYY/MM/DD) or press Enter to query all: ")
            task = input("Task (press Enter to skip): ")
            tag = input("Tag (press Enter to skip): ")
            records = tracker.query_time(date, task, tag)
            print("\nQuery results:")
            for record in records:
                print(f"{record[1]} {record[2]} - {record[3]}: {record[4]} ({record[5]})")

        elif choice == "3":
            start_date = input("Start Date (YYYY/MM/DD): ")
            end_date = input("End Date (YYYY/MM/DD): ")
            report = tracker.generate_report(start_date, end_date)
            print(report)

        elif choice == "4":
            result = tracker.priority_command()
            print(result)

        elif choice == "q":
            tracker.close()
            break