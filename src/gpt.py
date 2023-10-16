import tokenize
import io
import openai
import evadb
import os
import re

def preprocess_python_code(code):
    # Remove single line comments
    code = re.sub(r'#.*?\n', '\n', code)
    
    # Remove multi-line string literals (often used as comments)
    code = re.sub(r"'''(.*?)'''", '', code, flags=re.DOTALL)  # Remove triple-single-quoted strings
    code = re.sub(r'"""(.*?)"""', '', code, flags=re.DOTALL)  # Remove triple-double-quoted strings
    
    return code.strip()


# Initialize OpenAI API key
os.environ["OPENAI_KEY"] = "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"
openai.api_key = os.environ["OPENAI_KEY"]
import openai
import os


# Tokenize the code
def get_tokens(code):
    # Use the Python tokenize library or any other method to tokenize the code
    tokens = []
    for tok in tokenize.tokenize(io.BytesIO(code.encode('utf-8')).readline):
        tokens.append(tok.string)
    return ' '.join(tokens)

# Generate embeddings with OpenAI
def get_code_embedding(code: str) -> list:
    tokenized_code = get_tokens(code)
    response = openai.Embedding.create(input=tokenized_code, model="text-embedding-ada-002")
    embedding = response['data'][0]['embedding']
    return embedding

# Example usage
code_snippet = """
def add_numbers(a, b):
    return a + b
"""
code_snippet = preprocess_python_code(code_snippet)
embedding = get_code_embedding(code_snippet)
print(embedding)
