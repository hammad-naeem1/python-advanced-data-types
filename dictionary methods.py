
        # (               Dictionary Methods             )        


# 1.                    (  Creating a Dictionary)
 
# You can define a dictionary using curly braces {} with key: value syntax, or by using the dict() constructor.
# Creating a dictionary using curly braces
user = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "Data Science"]
}

# Creating an empty dictionary
empty_dict = {}


# ==========================


# 2.                 (Accessing and Modifying Items)

# You can look up values using square brackets [] or the safer .get() method.
# Accessing a value using brackets
print(user["name"])  # Output: Alice

# Using .get() prevents a KeyError if the key doesn't exist
print(user.get("status", "Not Found"))  # Output: Not Found

# Adding a new key-value pair or updating an existing one
user["location"] = "New York"  # Adds new item
user["age"] = 31               # Updates existing item

# =================================================



# 3.                     (Removing Items)

# Python offers multiple ways to delete data from a dictionary depending on your needs.
# Removes a specific key and returns its value
age = user.pop("age") 

# Removes a specific key without returning a value
del user["name"] 

# Removes and returns the last inserted key-value pair
last_item = user.popitem() 

# Empties the entire dictionary
user.clear() 


# ================================================


# 4.                     (Iterating Through a Dictionary)

# By default, looping over a dictionary iterates through its keys.
#  You can also explicitly target keys, values, or both.
inventory = {"apples": 10, "bananas": 5, "oranges": 8}

# Loop through keys
for fruit in inventory:
    print(fruit)

# Loop through values using .values()
for count in inventory.values():
    print(count)

# Loop through both using .items()
for fruit, count in inventory.items():
    print(f"We have {count} {fruit}")

# ==========================



# n             (Essential Dictionary Methods Reference)

# Method	                Description
# .get(key, default)	     Returns the value for a key; returns a default value (or None) if the key doesn't exist.
# .keys()	Returns            a view object containing all the keys in the dictionary.
# .values()	Returns              a view object containing all the values in the dictionary.
# .items()	Returns                 a view object containing tuples of (key, value) pairs.
# .update(other_dict)            	Merges another dictionary or iterable of pairs into the existing dictionary.
# .clear()	                      Removes all elements from the dictionary.



























































