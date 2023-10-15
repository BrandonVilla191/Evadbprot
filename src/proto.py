import os 
import evadb 
import samply.py




def read_codebase(directory):
    codebase = ""
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as f:
            codebase += f.read()
    return codebase


def generate_solution(prompt):
    return



def main():
    prompt = input("Enter a prompt: ")

    codebase = read_codebase("codebase")

    prompt = prompt + codebase

    solution = generate_solution(prompt)




