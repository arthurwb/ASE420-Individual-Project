import pytest
import sqlite3
import os
import sys

test_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(test_dir)
sys.path.append(root_dir)

from datetime import datetime, timedelta
from src.timetracker import TimeTracker

@pytest.fixture
def time_tracker():
    return TimeTracker(":memory:")

def test_record_time(time_tracker):
    date = "2023/01/01"
    start_time = "10:00 AM"
    end_time = "12:00 PM"
    task = "Test Task"
    tag = "Test Tag"

    success = time_tracker.record_time(date, start_time, end_time, task, tag)
    assert success is not None

    records = time_tracker.query_time()
    assert len(records) == 1

def test_generate_report(time_tracker):
    date = "2023/01/01"
    start_time = "10:00 AM"
    end_time = "12:00 PM"
    task = "Test Task"
    tag = "Test Tag"

    time_tracker.record_time(date, start_time, end_time, task, tag)
    report = time_tracker.generate_report(date, date)

    assert f"{date} {start_time} - {end_time}: {task} ({tag})" in report

def test_priority_command(time_tracker):
    date = "2023/01/01"
    start_time = "10:00 AM"
    end_time = "12:00 PM"
    task = "Test Task"
    tag = "Test Tag"

    for _ in range(5):
        time_tracker.record_time(date, start_time, end_time, task, tag)

    result = time_tracker.priority_command()
    assert f"{tag}: 5 occurrences" in result

def test_close(time_tracker):
    time_tracker.close()
    assert time_tracker.db_manager.conn is None
    with pytest.raises(AttributeError):
        time_tracker.db_manager.conn.cursor()

def test_record_multiple_times(time_tracker):
    date = "2023/01/01"
    start_time = "10:00 AM"
    end_time = "12:00 PM"
    task = "Test Task"
    tag = "Test Tag"

    time_tracker.record_time(date, start_time, end_time, task, tag)
    time_tracker.record_time(date, "01:00 PM", "02:00 PM", "Another Task", "Another Tag")

    records = time_tracker.query_time()
    assert len(records) == 2

def test_generate_report_multiple_entries(time_tracker):
    date = "2023/01/01"
    start_time = "10:00 AM"
    end_time = "12:00 PM"
    task = "Test Task"
    tag = "Test Tag"

    time_tracker.record_time(date, start_time, end_time, task, tag)
    time_tracker.record_time(date, "01:00 PM", "02:00 PM", "Another Task", "Another Tag")

    report = time_tracker.generate_report(date, date)

    assert f"{date} {start_time} - {end_time}: {task} ({tag})" in report
    assert f"{date} 01:00 PM - 02:00 PM: Another Task (Another Tag)" in report

def test_query_time_with_task_filter(time_tracker):
    date = "2023/01/01"
    start_time = "10:00 AM"
    end_time = "12:00 PM"
    task = "Test Task"
    tag = "Test Tag"

    time_tracker.record_time(date, start_time, end_time, task, "Tag1")
    time_tracker.record_time(date, "01:00 PM", "02:00 PM", task, "Tag2")

    records = time_tracker.query_time(task=task)

    assert len(records) == 2
    assert records[0][4] == task
    assert records[1][4] == task
