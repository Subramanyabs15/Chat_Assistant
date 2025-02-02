import sqlite3

# Define the database path
DATABASE_PATH = "database/employees.db"


# Connect to SQLite (Creates the file if it doesn't exist)
conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

# Create Employees Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Department TEXT NOT NULL,
        Salary INTEGER NOT NULL,
        Hire_Date TEXT NOT NULL
    )
''')

# Create Departments Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departments (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Manager TEXT NOT NULL
    )
''')

# Insert Sample Data
cursor.executemany('''
    INSERT INTO Employees (Name, Department, Salary, Hire_Date) VALUES (?, ?, ?, ?)
''', [
    ('Alice', 'Sales', 50000, '2021-01-15'),
    ('Bob', 'Engineering', 70000, '2020-06-10'),
    ('Charlie', 'Marketing', 60000, '2022-03-20')
])

cursor.executemany('''
    INSERT INTO Departments (Name, Manager) VALUES (?, ?)
''', [
    ('Sales', 'Alice'),
    ('Engineering', 'Bob'),
    ('Marketing', 'Charlie')
])

# Commit and close connection
conn.commit()
conn.close()

print("Database created successfully!")
