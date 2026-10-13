
        # (    Global and local variable                     )


# This is a GLOBAL variable
message = "I am global"

def my_function():
    # This is a LOCAL variable
    local_text = "I am local"
    
    print(local_text) # Works fine
    print(message)    # Works fine (functions can read global variables)

my_function()

print(message)    # Works fine
# print(local_text) # ERROR: NameError! The program doesn't know what local_text is out here.


# ========================================================================================================
    # 1. Modifying the Enclosing Scope (nonlocal)


def outer_func():
    x = "outer value"  # Enclosing scope
    
    def inner_func():
        nonlocal x     # Links to the outer function's 'x'
        x = "modified value"
        
    inner_func()
    print(x)           # Prints: "modified value"

outer_func()



# =============================================================

        # 2. Modifying the Global Scope (global)


x = "global value"     # Global scope

def outer_func():
    x = "outer value"  # Enclosing scope
    
    def inner_func():
        global x       # Links to the top-level 'x'
        x = "changed globally"
        
    inner_func()
    print("Outer:", x)  # Prints: Outer: outer value (unchanged!)

outer_func()
print("Global:", x)     # Prints: Global: changed globally




























