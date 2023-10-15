import evadb

# Set up the connection to the database
cursor = evadb.connect().cursor()

# Create a table to store the vectors
cursor.query("DROP TABLE IF EXISTS vectors").df()
querys = """CREATE TABLE vectors (
    id INTEGER PRIMARY KEY,
    vector TEXT(200)
);"""
cursor.query(querys).execute()
with open("sample.py", "r") as file:
    for line in file:
        if line.strip():
            print(line)
