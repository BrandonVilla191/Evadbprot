import evadb
import os
import pandas as pd
import re

def preprocess_python_code(code):
    # Remove single line comments
    code = re.sub(r'#.*?\n', '\n', code)
    
    # Remove multi-line string literals (often used as comments)
    code = re.sub(r"'''(.*?)'''", '', code, flags=re.DOTALL)  # Remove triple-single-quoted strings
    code = re.sub(r'"""(.*?)"""', '', code, flags=re.DOTALL)  # Remove triple-double-quoted strings
    
    return code.strip()

# Set the display options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)



os.environ["OPENAI_KEY"] = "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"

# Set up the connection to the database
cursor = evadb.connect().cursor()

# Create a table to store the vectors
cursor.query("DROP TABLE IF EXISTS vectors").execute()
querys = """CREATE TABLE vectors (
    id INTEGER PRIMARY KEY,
    vector TEXT(200)
);"""
print("Creating table...")
cursor.query(querys).execute()
print("Table created.")
count = 0
strin = ""
with open("sample.py", "r") as file:
    for line in file:
        if line.strip():
            strin += line
            
print("Inserting vectors...")
# Remove comments
code = preprocess_python_code(strin)
print("CODE", code)
query = f"INSERT INTO vectors (id, vector) VALUES (1, '{code}')"
print(cursor.query(query).execute())



print("chatgpt",cursor.query("""SELECT ChatGPT("Find the bug in this code. If there is a bug, give me ONLY the code changes and nothing else. No text, just code?" ,vector) FROM vectors;""").df())
# Close the connection to the database
cursor.close()
print("Connection closed.")
#
