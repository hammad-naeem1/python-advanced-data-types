
# 1.      (Unpacking Iterables in Function Calls (*))


def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]

# Without unpacking: add(numbers) raises a TypeError
# With unpacking: expands to add(1, 2, 3)
result = add(*numbers) 
print(result)  # Output: 6
# =========================================


# 2.    (Unpacking Dictionaries in Function Calls (**))

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

person = {"name": "Alice", "age": 30}

# Unpacks to introduce(name="Alice", age=30)
introduce(**person)  
# Output: My name is Alice and I am 30 years old.
# =========================((