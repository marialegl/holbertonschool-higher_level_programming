# Guide on how to perform MySQL operations from a Python script, and an explanation of ORM and class-to-table mapping.


### 1. **How to Connect to a MySQL Database from a Python Script**

To connect to a MySQL database, you can use the `mysql-connector-python` library. Here’s a step-by-step guide:

1. **Install the library**:
   ```bash
   pip install mysql-connector-python
   ```

2. **Connect to the database**:
   ```python
   import mysql.connector

   # Establish the connection
   connection = mysql.connector.connect(
       host='localhost',
       user='yourusername',
       password='yourpassword',
       database='yourdatabase'
   )

   # Check if connection is successful
   if connection.is_connected():
       print('Connected to MySQL database')
   ```

### 2. **How to SELECT Rows in a MySQL Table from a Python Script**

Use the `mysql-connector-python` library to execute a `SELECT` query:

```python
import mysql.connector

# Establish the connection
connection = mysql.connector.connect(
    host='localhost',
    user='yourusername',
    password='yourpassword',
    database='yourdatabase'
)

cursor = connection.cursor()

# Execute the SELECT query
cursor.execute("SELECT * FROM your_table")

# Fetch all rows
rows = cursor.fetchall()

# Iterate through the rows
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
```

### 3. **How to INSERT Rows in a MySQL Table from a Python Script**

Here’s how to insert rows into a MySQL table using Python:

```python
import mysql.connector

# Establish the connection
connection = mysql.connector.connect(
    host='localhost',
    user='yourusername',
    password='yourpassword',
    database='yourdatabase'
)

cursor = connection.cursor()

# Define the INSERT query
insert_query = """
INSERT INTO your_table (column1, column2)
VALUES (%s, %s)
"""

# Data to be inserted
data = ('value1', 'value2')

# Execute the INSERT query
cursor.execute(insert_query, data)

# Commit the transaction
connection.commit()

print(cursor.rowcount, "record inserted.")

# Close the cursor and connection
cursor.close()
connection.close()
```

### 4. **What ORM Means**

**ORM (Object-Relational Mapping)** is a programming technique used to convert data between incompatible type systems in object-oriented programming languages. It allows developers to interact with a database using the programming language's constructs, typically representing tables as classes and rows as objects.

**Advantages**:
- Simplifies database interactions.
- Provides abstraction over raw SQL queries.
- Enhances code maintainability and readability.

**Common Python ORMs**:
- SQLAlchemy
- Django ORM
- Peewee

### 5. **How to Map a Python Class to a MySQL Table**

Using an ORM like SQLAlchemy, you can map a Python class to a MySQL table. Here’s an example using SQLAlchemy:

1. **Install SQLAlchemy**:
   ```bash
   pip install SQLAlchemy
   ```

2. **Define the mapping**:
   ```python
   from sqlalchemy import create_engine, Column, Integer, String
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import sessionmaker

   # Define the base class
   Base = declarative_base()

   # Define the class mapping
   class User(Base):
       __tablename__ = 'users'
       id = Column(Integer, primary_key=True)
       name = Column(String(50))
       email = Column(String(50))

   # Create an engine
   engine = create_engine('mysql+mysqlconnector://yourusername:yourpassword@localhost/yourdatabase')

   # Create the table
   Base.metadata.create_all(engine)

   # Create a session
   Session = sessionmaker(bind=engine)
   session = Session()

   # Insert a new user
   new_user = User(name='John Doe', email='john@example.com')
   session.add(new_user)
   session.commit()
   ```

**Explanation**:
- **`Base = declarative_base()`**: Creates a base class for the mapped classes.
- **`__tablename__`**: Specifies the table name.
- **`Column`**: Maps attributes to columns in the table.
- **`engine`**: Connects to the MySQL database.
- **`session`**: Manages transactions and queries.

By using ORM, you can work with Python objects and classes instead of writing raw SQL, making your code more intuitive and easier to manage.
