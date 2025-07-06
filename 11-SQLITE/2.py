### Working with Sales Data
# Connect to an SQLite database
import sqlite3
connection = sqlite3.connect('sales_data.db')
cursor = connection.cursor()

# Create a table for sales data
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales(
    id INT PRIMARY KEY,
    date TEXT NOT NULL,
    product TEXT NOT NULL,
    sales INTEGER,
    region TEXT           
    )
''')

# Insert the data into the sales table
sales_data=[
    (1,'2023-01-01','Product1',100,'North'),
    (2,'2023-01-02','Product2',200,'South'),
    (3,'2023-01-03','Product1',100,'East'),
    (4,'2023-01-04','Product3',250,'West'),
    (5,'2023-01-05','Product2',300,'North'),
]

cursor.executemany('''
INSERT INTO sales(id,date,product,sales,region)
VALUES(?,?,?,?,?)
''',sales_data)

connection.commit()

# Query data from the sales table
cursor.execute('SELECT * FROM sales')
rows=cursor.fetchall()

# Print the queried data
for row in rows:
    print(row)