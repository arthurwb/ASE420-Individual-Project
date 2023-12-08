# Time Management Application Requirements

## User: Jack

### Record Time

1. **User Story:**
   - As Jack, I want to record my time usage using a command-line interface (CUI) with the following format: "DATE FROM TO TASK TAG".
   
2. **Format Flexibility:**
   - The application should allow Jack to specify the date using formats like "2022/09/23" and allow adding AM or PM to the FROM or TO time.

3. **Example Usage:**
   - Jack should be able to type the following command to record his time usage in the database:
     ```bash
     record today 09:30 10:30 'studied Java' :STUDY
     ```

### Query Time Usage

4. **User Story:**
   - As Jack, I want to query my time usage from the database using a CUI with the following options:
     - Query by DATE: "query today"
     - Query by TASK: "query 'Java'"
     - Query by TAG: "query :STUDY"

5. **Example Usage:**
   - Jack should be able to type the following commands to query his time usage:
     ```bash
     query today
     query 'Java'
     query :STUDY
     ```

## Additional Features Requested by Jack

### Generate Time Usage Report

6. **User Story:**
   - As Jack, I want to generate a time usage report within a specified date range, providing all activities during that period.

7. **Example Usage:**
   - Jack should be able to type the following command to generate a time usage report for the specified date range:
     ```bash
     report 2021/01/01 2022/01/01
     ```

### Priority Command

8. **User Story:**
   - As Jack, I want a priority command that provides a list of activities I spend the most time on.

9. **Example Usage:**
   - Jack should be able to type the following command to get a list of activities he spends the most time on:
     ```bash
     priority
     ```

## Technical Specifications

10. **Programming Language:**
    - The application should be developed using Python.

11. **Database:**
    - SQLite should be used for the database, leveraging Python's standard SQLite package.