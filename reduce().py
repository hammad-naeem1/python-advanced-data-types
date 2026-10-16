
    # (    REDUCE           )

    # The reduce() function in Python applies a two-argument function
    # cumulatively to the elements of an iterable, 
    # reducing the entire sequence down to a single final value. Unlike map() or filter(), 




# 1. Summing a List of Numbers (with lambda)

from functools import reduce

numbers = [2, 4, 6, 8]
# Process: ((2 + 4) + 6) + 8
total = reduce(lambda x, y: x + y, numbers)

print(total)  # Output: 20

# ======================================


# 2. Finding the Maximum Value

from functools import reduce

numbers = [5, 12, 3, 9]
# Tracks and passes the higher value to the next comparison
max_val = reduce(lambda x, y: x if x > y else y, numbers)

print(max_val)  # Output: 12

# =====================================
# 3. Using an Initializer


from functools import reduce

numbers = [1, 2, 3]
# Process: (((100 + 1) + 2) + 3)
total = reduce(lambda x, y: x + y, numbers, 100)

print(total)  # Output: 106
# ===============================================================


# 4. Using the operator Module (Most Efficient)

from functools import reduce
import operator

numbers = [1, 2, 3, 4]
product = reduce(operator.mul, numbers)

print(product)  # Output: 24 (1 * 2 * 3 * 4)
# ----------------------------------------------------------------------