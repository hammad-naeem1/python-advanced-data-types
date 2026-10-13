
#             (     FUNCTIONS       )

                # A Python function is a reusable block of code that only runs when it is called.



# 1. Defining the function
def greet():
    print("Hello! Welcome to Python.")

# 2. Calling the function
greet()

# --------------------

#                      ( Parameters and Arguments)


#  Parameters are the placeholders defined in the function creation.


#  Arguments are the actual values you pass into the function when you call it.

# example 
def greet_user(username):  # 'username' is a parameter
    print(f"Hello, {username}!")

greet_user("Alice")       # "Alice" is the argument
greet_user("Bob")         # "Bob" is a different argument


# ===================================================================

#                (          Returning a Value              ) 


# return statement. If a function does not have a return statement, 
# it automatically returns None by default.


def add_numbers(a, b):
    return a + b  # Sends the sum back to the caller

# Capture the returned value in a variable
result = add_numbers(5, 7)
print(result)  # Output: 12

# ==========================================

#             (          keyword arguments                 )


    # allow you to pass arguments to a function
    # by explicitly stating the parameter name and its value


def greet_user(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

# The order doesn't matter when using keyword arguments
greet_user(last_name="Skywalker", first_name="Luke")
# Output: Hello, Luke Skywalker!

# -----------------------------


#                     (   Default arguments   )
              
    # Default arguments in Python are parameters that have a 
    # predefined value assigned to them in the function definition.


# Function definition with a default argument
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()        # Output: Hello, Guest! (Uses the default value)
greet("Alice") # Output: Alice (Overrides the default value)
