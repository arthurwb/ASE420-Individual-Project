# Time Management System - User Requirements

## 1. Command Line Interface (CUI)
- As a user, I expect the system to have a Command Line Interface (CLI) that allows me to interact with the application using command-line tools.

## 2. Recording Time
- As a user (Jack), I want to record my time usage using the command format: `DATE FROM TO TASK TAG`.
- The system should support flexible date formats, such as "today" or "2022/09/23."
- AM or PM should be accepted for the FROM and TO times.

## 3. Querying Time
- As a user (Jack), I want to query my time usage from the database using the command format: `query DATE`, `query TASK`, or `query TAG`.
- For date queries, I expect to use formats like "today."
- Task queries should match activities containing the specified keyword.
- Tag queries should retrieve activities with the specified tag.

## 4. Flexibility in Query Format
- As a user, I expect the system to allow me to use flexible formats for queries, providing options like querying by date, task, or tag.

## 5. Programming Language and Database
- As a user, I expect the system to be implemented using Python as the programming language.
- SQLite should be used as the database, taking advantage of its integration with Python.

## 6. Error Handling
- As a user, I expect the system to handle errors gracefully and provide informative messages if there are issues with command input or database operations.

## 7. Database Storage
- As a user, I expect recorded time entries to be stored in an SQLite database.

## 8. DateTime Flexibility
- As a user (Jack), I expect the system to handle date and time flexibility, allowing me to enter information conveniently.

## 9. Data Retrieval
- As a user (Jack), I expect the system to retrieve and display relevant information from the database based on my queries.

## 10. User-Friendly Output
- As a user, I expect the system to present query results in a user-friendly and readable format.

## 11. Tagging System
- As a user, I want tags to be supported for categorizing activities.

## 12. Integration with Standard Python Libraries
- As a user, I expect the system to make use of standard Python libraries for simplicity and ease of use.