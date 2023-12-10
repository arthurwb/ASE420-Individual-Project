# Time Management Console Application

## Overview

The Time Management Console Application is a simple tool to help users record, query, and generate reports on their time usage. The application provides a Command Line Interface (CLI) for easy interaction.

## Table of Contents

- [Usage](#usage)
- [Features](#features)
- [Getting Started](#getting-started)
- [Technical Details](#technical-details)

## Usage

To use the Time Management Console Application, run the following script:

```bash
    python program.py
```

Replace `script_name.py` with the actual name of your Python script containing the application code.

## Features

1. **Record Time:**
   - Option to record time usage with date, start time, end time, task, and tag.

2. **Query Time:**
   - Option to query time records based on date, task, or tag.

3. **Generate Time Usage Report:**
   - Option to generate a time usage report for a specified date range.

4. **Priority Command:**
   - Option to view activities with the highest time spent.

5. **Database Storage:**
   - Time records are stored in an SQLite database.

## Getting Started

1. **Prerequisites:**
   - Ensure you have Python installed on your computer.
   - Familiarize yourself with accessing the terminal or command prompt.

2. **Run the Application:**
   - Open the terminal or command prompt.
   - Navigate to the directory containing the application script.
   - Run the script using the command mentioned in the [Usage](#usage) section.

3. **Interacting with the Application:**
   - Choose options (1/2/3/4/q) as per the menu prompts.
   - Follow the instructions to record time, query records, generate reports, or view priority commands.

## Technical Details

- The application is written in Python.
- SQLite is used for database storage.
- The `App` class in `app.py` contains the main application logic.
- The `TimeTracker` class in `timetracker.py` handles time-related functionality.
- The `DatabaseManager` class in `databasemanager.py` manages the SQLite database.

Feel free to explore and use the Time Management Console Application to enhance your time management skills! If you encounter any issues or have questions, refer to this readme or seek assistance from someone familiar with using the terminal.
