from nlp_processor import process_user_query

def parse_user_query(user_query):
    """
    Converts the processed NLP query into an SQL query.
    """
    extracted_info = process_user_query(user_query)

    print(f"🔹 Extracted NLP Info: {extracted_info}")  # Debugging Print

    department = extracted_info["department"]
    query_type = extracted_info["query_type"]
    date = extracted_info["date"]

    sql_query = None
    params = []

    if query_type == "manager" and department:
        sql_query = "SELECT Manager FROM Departments WHERE Name = ?"
        params = [department]

    elif query_type == "salary" and department:
        sql_query = "SELECT SUM(Salary) FROM Employees WHERE Department = ?"
        params = [department]

    elif query_type == "list_employees":
        if department:
            sql_query = "SELECT Name, Salary, Hire_Date FROM Employees WHERE Department = ?"
            params = [department]
        elif date:  # ✅ FIXED: Correctly handling date-based queries
            sql_query = "SELECT Name, Salary, Hire_Date FROM Employees WHERE Hire_Date > ?"
            params = [date]
        else:
            sql_query = "SELECT Name, Salary, Hire_Date FROM Employees"
            params = []  # No filters, return all employees

    else:
        print("❌ Could not generate SQL query!")  # Debugging Print
        return None  # Return None if NLP extraction failed

    print(f"✅ Generated SQL Query: {sql_query} with Params: {params}")  # Debugging Print
    return sql_query, params
