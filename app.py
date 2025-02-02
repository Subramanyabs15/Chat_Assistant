from flask import Flask, request, render_template, jsonify
from db_handler import execute_query
from query_parser import parse_user_query

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def chat():
    user_input = request.form.get("query", "")
    
    # Convert user query into SQL
    query_tuple = parse_user_query(user_input)

    if not query_tuple:
        response = "Sorry, I didn't understand the query."
        return render_template("index.html", response=response)

    sql_query, params = query_tuple
    results = execute_query(sql_query, params)

    return render_template("index.html", response=results)

if __name__ == '__main__':
    app.run(debug=True)
