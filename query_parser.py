import re

def parse_user_query(user_query):
    """
    Parses a natural language query and converts it into an SQL query.
    Returns an SQL query and its parameters.
    """

    # Show all employees in a department
    if "all employees in" in user_query.lower():
        dept = re.search(r"employees in the (\w+)", user_query, re.I)
        if dept:
            return "SELECT * FROM Employees WHERE Department = ?", (dept.group(1),)

    # Find the manager of a department
    if "who is the manager of" in user_query.lower():
        dept = re.search(r"manager of the (\w+)", user_query, re.I)
        if dept:
            return "SELECT Manager FROM Departments WHERE Name = ?", (dept.group(1),)

    # List employees hired after a certain date
    if "hired after" in user_query.lower():
        date = re.search(r"hired after (\d{4}-\d{2}-\d{2})", user_query, re.I)
        if date:
            return "SELECT * FROM Employees WHERE Hire_Date > ?", (date.group(1),)

    # Get total salary expense for a department
    if "total salary expense for" in user_query.lower():
        dept = re.search(r"salary expense for the (\w+)", user_query, re.I)
        if dept:
            return "SELECT SUM(Salary) FROM Employees WHERE Department = ?", (dept.group(1),)

    # Default case - unrecognized quer


def test_parser():
    test_queries = [
        "Show me all employees in the Sales department.",
        "Who is the manager of the Engineering department?",
        "List all employees hired after 2021-01-01.",
        "What is the total salary expense for the Marketing department?"
    ]

    for query in test_queries:
        print(f"User Query: {query}")
        result = parse_user_query(query)
        print(f"SQL Query: {result}\n")

if __name__ == "__main__":
    test_parser()

