# Chat_Assistant

# Chat Assistant for SQLite Database

## Overview
This project is a Python-based **Chat Assistant** that interacts with an SQLite database to answer user queries. The assistant accepts natural language input, converts it into SQL queries, retrieves data from the database, and presents clear, formatted responses.

## Features
- Accepts natural language queries.
- Converts user input into SQL queries.
- Retrieves relevant data from an SQLite database.
- Handles invalid queries and errors gracefully.
- Supports various types of queries, including:
  - "Show me all employees in the [department] department."
  - "Who is the manager of the [department] department?"
  - "List all employees hired after [date]."
  - "What is the total salary expense for the [department] department?"

## Technologies Used
- **Python** (Core programming language)
- **SQLite** (Database management)
- **Flask/FastAPI** (For API handling, optional for deployment)
- **NLTK or spaCy** (For processing natural language queries, if needed)
- **SQLAlchemy** (For database interaction)

## Getting Started

### 1. Clone the Repository
```sh
 git clone https://github.com/your-username/chat-assistant-sqlite.git
 cd chat-assistant-sqlite
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```sh
 python -m venv venv
 source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
 pip install -r requirements.txt
```

### 4. Prepare the Database
The project uses an SQLite database. Ensure you have an `employees.db` file with the following schema:

```sql
CREATE TABLE Employees (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Department TEXT NOT NULL,
    Salary INTEGER NOT NULL,
    Hire_Date TEXT NOT NULL
);

CREATE TABLE Departments (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Manager TEXT NOT NULL
);
```
You can populate it with sample data before running the assistant.

### 5. Run the Assistant
#### If using a Python script:
```sh
 python chat_assistant.py
```

#### If using Flask/FastAPI:
```sh
 python app.py
```
Access the assistant via `http://127.0.0.1:5000` (for Flask) or the provided URL (for FastAPI).

## How It Works
1. The user enters a query in natural language.
2. The assistant processes the query and maps it to an SQL command.
3. The assistant queries the SQLite database.
4. The retrieved data is formatted and returned as a response.
5. The assistant provides meaningful messages for invalid inputs.

## Error Handling
- Invalid department names return an appropriate error message.
- Queries with incorrect formats prompt the user to rephrase.
- If no results are found, the assistant informs the user.

## Known Limitations & Future Improvements
- **Limited NLP Support**: The assistant may not handle complex sentence structures well.
- **Enhancements Needed for Complex Queries**: Support for multi-condition queries can be improved.
- **Deployment**: Currently runs locally; future versions can be deployed to cloud platforms.
- **User Authentication**: Future improvements may include authentication and authorization.

## Contribution
Feel free to fork the repository and submit pull requests with improvements!

## License
This project is open-source and available under the [MIT License](LICENSE).

