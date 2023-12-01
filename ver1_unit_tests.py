import pytest
import sqlite3
from datetime import datetime
from program import TimeTracker

@pytest.fixture
def in_memory_database():
    conn = sqlite3.connect(':memory:')
    yield conn
    conn.close()

@pytest.fixture
def time_tracker(in_memory_database):
    tracker = TimeTracker(":memory:")
    return tracker

def test_create_table(time_tracker):
    cursor = time_tracker.conn.cursor()
    cursor.execute("PRAGMA table_info(time_records);")
    columns = cursor.fetchall()
    assert len(columns) == 6

def test_record_time(time_tracker):
    date = "2023/01/01"
    start_time = "10:00 AM"
    end_time = "12:00 PM"
    task = "Test Task"
    tag = "Test Tag"

    time_tracker.record_time(date, start_time, end_time, task, tag)

    cursor = time_tracker.conn.cursor()
    cursor.execute("SELECT * FROM time_records;")
    records = cursor.fetchall()

    assert len(records) == 1
    assert records[0][1] == date
    assert records[0][2] == start_time
    assert records[0][3] == end_time
    assert records[0][4] == task
    assert records[0][5] == tag

def test_query_time(time_tracker):
    date = "2023/01/01"
    task = "Test Task"
    tag = "Test Tag"

    time_tracker.record_time(date, "10:00 AM", "12:00 PM", task, tag)

    records = time_tracker.query_time(date, task, tag)

    assert len(records) == 1
    assert records[0][1] == date
    assert records[0][4] == task
    assert records[0][5] == tag

def test_close(time_tracker):
    time_tracker.close()
    with pytest.raises(sqlite3.ProgrammingError):
        time_tracker.conn.cursor()