import pytest
from unittest.mock import patch
from io import StringIO
import os
import sys

test_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(test_dir)
sys.path.append(root_dir)

from src.timetracker import TimeTracker
from src.app import App

@pytest.fixture
def time_tracker_instance():
    return TimeTracker(":memory:")

def test_query_time(time_tracker_instance):
    with patch("builtins.input", side_effect=["2", "today", "", "", "q"]):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            App.run()

    output = mock_stdout.getvalue().strip()
    assert "Query results:" in output

def test_generate_report(time_tracker_instance):
    with patch("builtins.input", side_effect=["3", "2022/01/01", "2022/12/31", "q"]):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            App.run()

    output = mock_stdout.getvalue().strip()
    assert "Time Usage Report (2022/01/01 to 2022/12/31):" in output

def test_priority_command(time_tracker_instance):
    with patch("builtins.input", side_effect=["4", "q"]):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            App.run()

    output = mock_stdout.getvalue().strip()
    assert "Activities with the highest time spent:" in output