from collections import Counter
from src.databasemanager import DatabaseManager

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
        return True

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
        if (end_date == None):
            end_date = start_date
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
        self.db_manager.conn = None