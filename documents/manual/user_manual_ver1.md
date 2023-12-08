# Time Tracking Application Manual

Welcome to the Time Tracking Application! This manual will guide you through the features and functionalities of the application, helping you make the most out of your time tracking experience.

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Recording Time](#recording-time)
4. [Querying Time Records](#querying-time-records)
5. [Generating Time Usage Report](#generating-time-usage-report)
6. [Priority Command](#priority-command)
7. [Exiting the Application](#exiting-the-application)

## Introduction

The Time Tracking Application is a simple tool designed to help you record and analyze your daily activities. It provides features to record time spent on tasks, query time records based on specific criteria, generate time usage reports, and identify activities with the highest time spent.

## Getting Started

1. **Launch the Application:**
   - Run the `main.py` file to start the application.

2. **Initialization:**
   - The application will initialize a SQLite database (`time_tracker.db`) to store time records.

## Recording Time

### Option 1: Record Time
- Select option `1` to record time.
- Enter the following details:
  - Date (YYYY/MM/DD or today)
  - Start time (HH:MM AM/PM)
  - End time (HH:MM AM/PM)
  - Task
  - Tag
- Your time will be recorded, and a success message will be displayed.

## Querying Time Records

### Option 2: Query Time
- Select option `2` to query time records.
- Enter the criteria for the query:
  - Date (YYYY/MM/DD) or press Enter to query all
  - Task (press Enter to skip)
  - Tag (press Enter to skip)
- The query results will be displayed, showing date, start time, end time, task, and tag.

## Generating Time Usage Report

### Option 3: Generate Time Usage Report
- Select option `3` to generate a time usage report.
- Enter the start date (YYYY/MM/DD) and end date (YYYY/MM/DD).
- A report will be generated, summarizing time records between the specified dates.

## Priority Command

### Option 4: Activities with Highest Time Spent (Priority Command)
- Select option `4` to view activities with the highest time spent.
- The system will display the top activities along with the number of occurrences.

## Exiting the Application

### Option q: Exit
- Select option `q` to exit the application.
- Your data will be saved, and the application will close.