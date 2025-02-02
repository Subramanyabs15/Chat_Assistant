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

if __name__ == '__main__':
    app.run(debug=True)
