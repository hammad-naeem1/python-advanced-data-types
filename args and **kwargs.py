
    #       (   *args and **kwargs               )

    # *args and **kwargs allow a function to accept a variable number of arguments, 
    # making your functions highly flexible and dynamic




# 1.         (args (Positional Arguments))
def sum_numbers(*args):
    # args is a tuple: (10, 20, 30)
    return sum(args)

print(sum_numbers(10, 20, 30))  # Output: 60
print(sum_numbers(5, 5))        # Output: 10

# ==========================


# 2.          (**kwargs (Keyword Arguments))

def build_profile(**kwargs):
    # kwargs is a dictionary: {'name': 'Alice', 'age': 28, 'role': 'Engineer'}
    for key, value in kwargs.items():
        print(f"{key}: {value}")

build_profile(name="Alice", age=28, role="Engineer")
# ===================================



# 3.             (  Combining *args and **kwargs     )



def master_function(required_arg, *args, **kwargs):
    print(f"Required: {required_arg}")
    print(f"Args tuple: {args}")
    print(f"Kwargs dict: {kwargs}")

master_function("Main", "extra1", "extra2", debug=True, speed="fast")









