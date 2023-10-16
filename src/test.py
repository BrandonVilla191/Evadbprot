import evadb

# Set up the connection to the database
cursor = evadb.connect().cursor()

# Create a table to store the vectors
cursor.query("DROP TABLE IF EXISTS vectors").execute()
querys = """
CREATE TABLE vectors (
    id INTEGER PRIMARY KEY,
    vector TEXT(200)
);
"""
cursor.query(querys).execute()
print("Table created.")
# Sample code snippets (just for demonstration)
vectors = [
    (1, "0.1,0.2,0.3"),  # Vector for some code snippet
    (2, "0.4,0.5,0.6"),  # Vector for some other code snippet
    # ... add more as needed
]
print("Inserting vectors...")
for vector in vectors:
    query = f"INSERT INTO vectors (id, vector) VALUES ({vector[0]}, '{vector[1]}')"
    cursor.query(query).execute()


# Create a dummy function for CodeFeatureExtractor
cursor.query("""
    CREATE FUNCTION CodeFeatureExtractor(input TEXT) 
    RETURNS TEXT AS $$
        BEGIN
            RETURN input;  # Simply return the input
        END;
    $$ LANGUAGE plpgsql;
""").execute()


print("Vectors inserted.")
cursor.query("""
    CREATE INDEX code_vector_index
    ON vectors (CodeFeatureExtractor(vector))
    USING FAISS;
""").execute()

user_input = "Function is subtracting instead of adding"
query_vector = "0.15,0.25,0.35"  # This should be generated using some method, but just for demonstration




result = cursor.query(f"""
    SELECT vector FROM vectors 
    ORDER BY Similarity(CodeFeatureExtractor('{query_vector}')), vector) 
    LIMIT 5
""").df()

print(result)


