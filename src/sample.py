def add_numbers(a, b):
    return a - b  # Bug: This should be addition, but it's subtraction

if __name__ == "__main__":
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")


#The bug is that the function is subtracting instead of adding.