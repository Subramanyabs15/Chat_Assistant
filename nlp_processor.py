import spacy
import re

nlp = spacy.load("en_core_web_sm")

def process_user_query(user_query):
    """
    Processes a natural language query and extracts structured components for SQL conversion.
    """
    doc = nlp(user_query.lower())

    department = None
    query_type = None
    date = None

    # Identify named entities and key terms
    for token in doc:
        print(f"🔍 Token: {token.text} | Entity: {token.ent_type_}")  # Debugging print

        if token.ent_type_ == "ORG" or token.text.lower() in ["sales", "engineering", "marketing"]:
            department = token.text.capitalize()
        if token.text in ["manager", "head"]:
            query_type = "manager"
        if token.text in ["salary", "total salary", "payroll"]:
            query_type = "salary"
        if token.text in ["employees", "staff", "workers"]:  # New condition for listing employees
            query_type = "list_employees"
        if re.match(r"\d{4}-\d{2}-\d{2}", token.text):  # Matches YYYY-MM-DD format
            date = token.text

    # Debugging Output
    print(f"🛠 NLP Extracted: department={department}, query_type={query_type}, date={date}")

    return {
        "department": department,
        "query_type": query_type,
        "date": date
    }
