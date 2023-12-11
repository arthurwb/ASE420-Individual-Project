from datetime import datetime
from dateutil import parser
from src.timetracker import TimeTracker

class App:
    def run():
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
                    date = datetime.today().strftime('%Y/%m/%d')
                start_time = input("Start time (HH:MM AM/PM): ")
                end_time = input("End time (HH:MM AM/PM): ")
                task = input("Task: ")
                tag = input("Tag: ")

                tracker.record_time(date, start_time, end_time, task, tag)

            elif choice == "2":
                date = input("Date (YYYY/MM/DD) or press Enter to query all: ")
                task = input("Task (press Enter to skip): ")
                tag = input("Tag (press Enter to skip): ")
                records = tracker.query_time(start_date=date, task=task, tag=tag)
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