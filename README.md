# Chat_Assistant

Chat_Assistant
Python-based Chat Assistant for SQLite Database
🚀 Live API:
🔗 https://chatassistant-production-2fb6.up.railway.app

📌 Overview
This project is a Flask-based Chat Assistant that interacts with an SQLite database to answer user queries.
It accepts natural language input, converts it into SQL queries, fetches data, and responds in a clear, formatted manner.

📌 Features
✅ Accepts natural language queries.
✅ Converts user input into SQL queries.
✅ Retrieves relevant data from an SQLite database.
✅ Handles invalid queries & errors gracefully.
✅ Supports various queries, including:

"Show me all employees in the [department] department."
"Who is the manager of the [department] department?"
"List all employees hired after [date]."
"What is the total salary expense for the [department] department?"
📌 Technologies Used
Python (Core programming language)
SQLite (Database management)
Flask (Web API)
NLTK (For natural language processing, if needed)
SQLAlchemy (For database interaction)
📌 Getting Started
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/Subramanyabs15/Chat_Assistant.git
cd Chat_Assistant
2️⃣ Set Up a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Prepare the SQLite Database
Ensure employees.db exists with this schema:

sql
Copy
Edit
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
If missing, create it manually or use create_db.py.

5️⃣ Run the Assistant
bash
Copy
Edit
python app.py
The API will be accessible at:
cpp
Copy
Edit
http://127.0.0.1:5000
If using Railway, use your live URL:
arduino
Copy
Edit
https://chatassistant-production-2fb6.up.railway.app
📌 API Endpoints
Method	Endpoint	Description
GET	/	Returns "Chat Assistant API is running!"
POST	/chat	Accepts a user query and returns results
📌 Example API Requests
📝 1️⃣ Using curl (Command Line)
bash
Copy
Edit
curl -X POST "https://chatassistant-production-2fb6.up.railway.app/chat" \
-H "Content-Type: application/json" \
-d '{"query": "Who is the manager of the Sales department?"}'
📝 2️⃣ Using Postman
Method: POST
URL: https://chatassistant-production-2fb6.up.railway.app/chat
Headers: { "Content-Type": "application/json" }
Body (JSON):
json
Copy
Edit
{
    "query": "Who is the manager of the Sales department?"
}
✅ Expected Response:

json
Copy
Edit
{"response": [["Alice"]]}
📌 How It Works
User enters a query in natural language.
Query gets converted into SQL using query_parser.py.
SQLite database fetches relevant data.
The response is formatted & returned in JSON.
📌 Error Handling
✔ Handles invalid department names (returns appropriate message).
✔ Gracefully manages incorrect query formats.
✔ Returns “No results found” for queries with no matching data.

📌 Known Limitations & Future Improvements
🚧 Limited NLP Support: Complex sentence handling can be improved.
🚧 Enhancements Needed for Multi-Condition Queries.
🚧 User Authentication: Not yet implemented, could be a future feature.

📌 Contribution
Feel free to fork the repository and submit pull requests with improvements!
Your contributions are welcome! 😊🎯

## License
This project is open-source and available under the [MIT License](LICENSE).

