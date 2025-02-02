import sqlite3
import os
DATABASE_PATH = os.path.join(os.path.dirname(__file__), "employees.db")


# Define the database path
DATABASE_PATH = "database/employees.db"

# Function to connect to the database
def connect_db():
    return sqlite3.connect(DATABASE_PATH)

# Function to execute queries
def execute_query(query, params=()):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

def test_query():
    query = "SELECT * FROM Employees"
    results = execute_query(query)
    for row in results:
        print(row)

if __name__ == "__main__":
    test_query()

