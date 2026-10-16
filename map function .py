
        #   (       MAP        )
# map() function executes a specified function for each item
# in one or more iterables and returns a lazy iterator (a map object)



# example :

# Convert a list of strings into integers
string_numbers = ["1", "2", "3", "4"]
integers = list(map(int, string_numbers))

print(integers) 
# Output: [1, 2, 3, 4]



# example with lambda:

# Square every number in a list
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))

print(squared) 
# Output: [1, 4, 9, 16]





