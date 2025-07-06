### SQL And SQLite

## SQL(Structured Query Language) is a standard language for managing and manipulating relational databases. SQLite is a self-contained, serverless, and zero-configuraion database engine that is widely used for embedded database systems. In this lesson, we will cover the basics of SQL and SQLite, including creating databases, tables, and performing various SQL operations.

import sqlite3

## Connect to an SQLite database
connection=sqlite3.connect('example.db')

## Creating the cursor
cursor=connection.cursor()

## Creating a Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees(
    id INT PRIMARY KEY,
    name TEXT NOT NULL,
    age INT,
    department TEXT
    )
''')

## Commit the Changes
connection.commit()

cursor.execute('''
    SELECT * FROM employees
''')

# Insert the data into sqlite table
# cursor.execute('''
# INSERT INTO employees(id,name,age,department)
#             values(192,'Ibraheem',23,'NLP Engineer')
# ''')

# cursor.execute('''
# INSERT INTO employees(id,name,age,department)
#             values(326,'Safiullah',24,'DEVOPS Engineer')
# ''')

# cursor.execute('''
# INSERT INTO employees(id,name,age,department)
#             values(216,'Ashiq',22,'MERN STACK Engineer')
# ''')

# cursor.execute('''
# INSERT INTO employees(id,name,age,department)
#             values(195,'Dawood',22,'Trader')
# ''')
connection.commit()

## Query the data from the table
cursor.execute('SELECT * FROM employees')
rows=cursor.fetchall()
for row in rows:
    print(row)

## update the data in the table
cursor.execute('''
UPDATE employees
SET name='Muhammad Ibraheem'
WHERE id=192
''')

connection.commit()

cursor.execute('SELECT * FROM employees')
rows=cursor.fetchall()
for row in rows:
    print(row)

## Delete the data from the table
cursor.execute('''
DELETE FROM employees
WHERE name='Dawood'
''')

connection.commit()

cursor.execute('SELECT * FROM employees')
rows=cursor.fetchall()
for row in rows:
    print(row)