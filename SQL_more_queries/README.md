# SQL MORE QUERIES

### 1. **How to Create a New MySQL User**
To create a new MySQL user, you can use the `CREATE USER` statement followed by the `GRANT` statement to set permissions. Here's an example:

```sql
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost';
```

- `newuser`: The name of the new user.
- `localhost`: Specifies where the user can connect from (can be `%` for any host).
- `password`: The password for the new user.

### 2. **How to Manage Privileges for a User to a Database or Table**
Use the `GRANT` statement to assign privileges and the `REVOKE` statement to remove them. Examples:

- Granting all privileges on a specific database:
  ```sql
  GRANT ALL PRIVILEGES ON `database_name`.* TO 'username'@'host';
  ```

- Granting specific privileges on a table:
  ```sql
  GRANT SELECT, INSERT ON `database_name`.`table_name` TO 'username'@'host';
  ```

- Revoking privileges:
  ```sql
  REVOKE INSERT ON `database_name`.`table_name` FROM 'username'@'host';
  ```

### 3. **What’s a PRIMARY KEY**
A `PRIMARY KEY` is a unique identifier for a record in a table. It ensures that each row in the table is unique and that the column(s) used as the primary key cannot contain `NULL` values. 

Example:
```sql
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    PRIMARY KEY (EmployeeID)
);
```

### 4. **What’s a FOREIGN KEY**
A `FOREIGN KEY` is a field (or collection of fields) in one table that uniquely identifies a row of another table. It creates a link between the two tables.

Example:
```sql
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    OrderNumber INT,
    CustomerID INT,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
```

### 5. **How to Use NOT NULL and UNIQUE Constraints**
- `NOT NULL`: Ensures that a column cannot have `NULL` values.
  ```sql
  CREATE TABLE Products (
      ProductID INT,
      ProductName VARCHAR(255) NOT NULL
  );
  ```

- `UNIQUE`: Ensures that all values in a column are different.
  ```sql
  CREATE TABLE Users (
      UserID INT,
      Email VARCHAR(255) UNIQUE
  );
  ```

### 6. **How to Retrieve Data from Multiple Tables in One Request**
To retrieve data from multiple tables, you can use `JOIN` clauses or subqueries.

- Using `JOIN`:
  ```sql
  SELECT Orders.OrderID, Customers.CustomerName
  FROM Orders
  INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
  ```

- Using subqueries:
  ```sql
  SELECT CustomerName 
  FROM Customers 
  WHERE CustomerID IN (SELECT CustomerID FROM Orders WHERE OrderDate = '2024-06-01');
  ```

### 7. **What are Subqueries**
A subquery is a query nested inside another query. Subqueries can be used in `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statements or inside another subquery. They often provide data to the main query.

Example:
```sql
SELECT * FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);
```

### 8. **What are JOIN and UNION**
- `JOIN`: Combines rows from two or more tables based on a related column between them.
  - `INNER JOIN`: Returns records that have matching values in both tables.
    ```sql
    SELECT * FROM Orders
    INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
    ```
  - `LEFT JOIN` (or `LEFT OUTER JOIN`): Returns all records from the left table, and the matched records from the right table.
    ```sql
    SELECT * FROM Orders
    LEFT JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
    ```

- `UNION`: Combines the result sets of two or more `SELECT` statements into a single result set. Each `SELECT` must have the same number of columns in the result sets with similar data types.
  ```sql
  SELECT City FROM Customers
  UNION
  SELECT City FROM Suppliers;
  ```

