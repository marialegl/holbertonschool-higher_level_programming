Sure, here are the answers to each of those questions:

1. **What’s a database?**
   - A database is an organized collection of data, typically stored and accessed electronically from a computer system. It is structured to allow easy retrieval, insertion, and management of data.

2. **What’s a relational database?**
   - A relational database is a type of database that stores and provides access to data points that are related to one another. It organizes data into tables (or relations) where each table consists of rows (records) and columns (attributes or fields). Relationships between tables are established using keys.

3. **What does SQL stand for?**
   - SQL stands for Structured Query Language. It is a domain-specific language used in programming and designed for managing data held in a relational database management system (RDBMS) or for stream processing in a relational data stream management system (RDSMS).

4. **What’s MySQL?**
   - MySQL is an open-source relational database management system (RDBMS) based on SQL. It is one of the most widely used database systems for web applications due to its speed and reliability.

5. **How to create a database in MySQL?**
   - To create a database in MySQL, you typically use the following SQL command:
     ```sql
     CREATE DATABASE database_name;
     ```

6. **What does DDL and DML stand for?**
   - DDL stands for Data Definition Language. It includes SQL commands used to define and modify the structure of database objects (like tables and schemas).
   - DML stands for Data Manipulation Language. It includes SQL commands used to manipulate the data within the database (like inserting, updating, and deleting records).

7. **How to CREATE or ALTER a table?**
   - To create a new table in MySQL:
     ```sql
     CREATE TABLE table_name (
         column1 datatype constraints,
         column2 datatype constraints,
         ...
     );
     ```
   - To alter an existing table (add a column, for example):
     ```sql
     ALTER TABLE table_name
     ADD column_name datatype;
     ```

8. **How to SELECT data from a table?**
   - To retrieve data from a table in MySQL:
     ```sql
     SELECT column1, column2, ...
     FROM table_name
     WHERE condition;
     ```

9. **How to INSERT, UPDATE or DELETE data?**
   - To insert data into a table:
     ```sql
     INSERT INTO table_name (column1, column2, ...)
     VALUES (value1, value2, ...);
     ```
   - To update data in a table:
     ```sql
     UPDATE table_name
     SET column1 = value1, column2 = value2, ...
     WHERE condition;
     ```
   - To delete data from a table:
     ```sql
     DELETE FROM table_name
     WHERE condition;
     ```

10. **What are subqueries?**
    - Subqueries (also known as nested queries or inner queries) are queries nested inside another SQL query. They allow you to use the result of one query as input for another query.

11. **How to use MySQL functions?**
    - MySQL provides a wide range of built-in functions for performing operations on data. You can use functions like `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`, string functions (`SUBSTRING`, `CONCAT`, etc.), date functions (`DATE_FORMAT`, `NOW`, etc.), and many more in your SQL queries.