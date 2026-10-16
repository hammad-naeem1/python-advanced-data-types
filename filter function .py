
        #       (           filter                    )


# The filter() function in Python extracts elements from an iterable 
# (like a list, tuple, or set) that satisfy a specific condition



# 1. Using a lambda function (Most Common)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter out only the even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  
# Output: [2, 4, 6, 8, 10]


# ====================================================
# 2. Using a Custom / Named Function

def is_long_word(word):
    return len(word) > 5

words = ["apple", "banana", "kiwi", "cherry", "fig"]

# Filter out words longer than 5 letters
long_words = list(filter(is_long_word, words))

print(long_words)  
# Output: ['banana', 'cherry']


# ==============================================
# 3. Using None to Remove Falsy Values

mixed_data = [1, 0, "hello", "", False, True, None, "world"]

# Remove all falsy values
clean_data = list(filter(None, mixed_data))

print(clean_data)  
# Output: [1, 'hello', True, 'world']
