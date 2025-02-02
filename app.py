from flask import Flask, request, jsonify
from db_handler import execute_query
from query_parser import parse_user_query

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    """
    Receives a user query, processes it, and returns the result.
    """
    user_input = request.json.get("query", "")

    # Convert user query into SQL
    query_tuple = parse_user_query(user_input)

    if not query_tuple:
        return jsonify({"response": "Sorry, I didn't understand the query."})

    sql_query, params = query_tuple
    results = execute_query(sql_query, params)

    return jsonify({"response": results})
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Get port from Railway
    app.run(host='0.0.0.0', port=port, debug=True)


