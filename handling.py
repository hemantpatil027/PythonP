def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Input must be numbers")
    return a + b
print(add(1,3.5))
