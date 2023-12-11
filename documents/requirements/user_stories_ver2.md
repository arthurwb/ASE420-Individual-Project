# Time Management Application Requirements

## User: Jack

### Record Time

1. **User Story:**
   - As a user, I want to record my time usage using a command-line interface (CUI) with the following format: "DATE FROM TO TASK TAG".

2. **Format Flexibility:**
   - As a user, I expect the application to allow me to specify the date using formats like "2022/09/23" and enable adding AM or PM to the FROM or TO time.

3. **Example Usage:**
   - As a user, I would want to type the following command to record my time usage in the database:
     ```bash
     record today 09:30 10:30 'studied Java' STUDY
     ```

### Query Time Usage

4. **User Story:**
   - As a user, I expect to query my time usage from the database using a CUI with the following options:
     - Query by DATE: "query today"
     - Query by TASK: "query 'Java'"
     - Query by TAG: "query STUDY"

5. **Example Usage:**
   - As a user, I would want to type the following commands to query my time usage:
     ```bash
     query today
     query 'Java'
     query STUDY
     ```

## Additional Features Requested by Jack

### Generate Time Usage Report

6. **User Story:**
   - As a user, I would want to generate a time usage report within a specified date range, providing all activities during that period.

7. **Example Usage:**
   - As a user, I expect to type the following command to generate a time usage report for the specified date range:
     ```bash
     report 2021/01/01 2022/01/01
     ```

### Priority Command

8. **User Story:**
   - As a user, I would want a priority command that provides a list of activities I spend the most time on.

9. **Example Usage:**
   - As a user, I expect to type the following command to get a list of activities I spend the most time on:
     ```bash
     priority
     ```

## Technical Specifications

10. **Programming Language:**
    - As a user, I expect the application to be developed using Python.

11. **Database:**
    - As a user, I expect SQLite to be used for the database, leveraging Python's standard SQLite package.
