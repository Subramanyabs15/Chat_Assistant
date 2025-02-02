from flask import Flask, request, jsonify, render_template
from db_handler import execute_query
from query_parser import parse_user_query

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")  # Load the web page

@app.route('/query', methods=['POST'])
def query():
    """
    Receives a user query, processes it, and returns the result.
    """
    user_input = request.form.get("query", "").strip()

    if not user_input:
        return render_template("index.html", response="⚠️ Please enter a query.")

    # Convert user query into SQL
    query_tuple = parse_user_query(user_input)

    if not query_tuple:
        return render_template("index.html", response="❌ Sorry, I didn't understand the query.")

    sql_query, params = query_tuple
    results = execute_query(sql_query, params)

    # Format response properly
    if results:
        formatted_response = "<br>".join(
            [f"👤 {row[0]} | 💰 Salary: {row[1]} | 📅 Hired: {row[2]}" if len(row) > 2 
             else f"{row[0]}" for row in results]
        )
    else:
        formatted_response = "⚠️ No results found."

    return render_template("index.html", response=formatted_response)

if __name__ == '__main__':
    app.run(debug=True)
