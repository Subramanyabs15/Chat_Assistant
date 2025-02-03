import spacy
import re
import os

# Ensure the model is installed
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])

# ✅ Define a set of department names for better matching
DEPARTMENTS = {"sales", "engineering", "marketing", "hr"}

def extract_date(query):
    """Extracts date in YYYY-MM-DD format from a query string."""
    match = re.search(r"\b\d{4}-\d{2}-\d{2}\b", query)
    return match.group() if match else None

def process_user_query(user_query):
    """
    Processes a natural language query and extracts structured components for SQL conversion.
    """
    doc = nlp(user_query.lower())

    department = None
    query_type = None
    date = extract_date(user_query)  # ✅ Extract date from the entire query

    # Identify named entities and key terms
    for token in doc:
        print(f"🔍 Token: {token.text} | Entity: {token.ent_type_}")  # Debugging print

        # ✅ Match department names
        if token.text.lower() in DEPARTMENTS:
            department = token.text.capitalize()

        # ✅ Query type detection
        if token.text in ["manager", "head"]:
            query_type = "manager"
        if token.text in ["salary", "total salary", "payroll"]:
            query_type = "salary"
        if token.text in ["employees", "staff", "workers", "list"]:  # ✅ More keywords for listing
            query_type = "list_employees"

    # ✅ Handle "hired after" or "joined after" queries
    if "hired after" in user_query.lower() or "joined after" in user_query.lower():
        query_type = "list_employees"

    # Debugging Output
    print(f"🛠 NLP Extracted: department={department}, query_type={query_type}, date={date}")

    return {
        "department": department,
        "query_type": query_type,
        "date": date
    }
