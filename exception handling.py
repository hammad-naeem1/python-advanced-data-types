
#   exception handling 

    #  exception in Python is a runtime error that occurs
    # during the execution of a program, disrupting its normal flow

try:
    # Code that might cause an error
    numerator = 10
    denominator = int(input("Enter a divisor: "))
    result = numerator / denominator

except ZeroDivisionError:
    # Executes ONLY if a ZeroDivisionError occurs
    print("Error: You cannot divide by zero!")

except ValueError:

    # Executes ONLY if the input cannot be turned into an integer
    print("Error: Please enter a valid number!")

except Exception as e:
    # Catch-all for any other unforeseen exception
    print(f"An unexpected error occurred: {e}")

else:
    # Executes ONLY if the try block ran completely error-free
    print(f"Success! The result is {result}")

finally:
    # ALWAYS executes, whether an error happened or not (used for cleanup)
    print("Execution complete. Cleaning up resources.")


# ==========================================================================================
            # (        Bulid in exceptions                 )

# ZeroDivisionError: Trying to divide a number by zero.

# ValueError: A function receives an argument of the right type but inappropriate value (e.g., int("apple")).

# TypeError: Applying an operation to an inappropriate data type (e.g., 'abc' + 5).

# FileNotFoundError: Attempting to open or read a file path that doesn't exist.

# IndexError: Attempting to access an index out of a list's range.

# KeyError: Looking up a dictionary key that does not exist







