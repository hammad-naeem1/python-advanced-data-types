
                  #  (     # list comprehension          )

    # a concise, single-line syntax used to create new lists from existing iterables. 
    # Ierate at allows you to gen new list by applying an expression to each item in an 
    # iterable, optionally filtering items based on a condition.

        #    (1)what to kepp   (2) for each item   (3)in collection

# EXAMPLE:
square=[i**2 for i in range (1,6) if i%2==0]
print(square)

# second_example 
names=['spiderman','Loki','scarlett johanson🫀','Ironman','Thor','hulk']
capital_names=[n for n in names if n[0].isupper()]
print(capital_names)

  # ==============================================================================================
               # (     nested   comprehension         )
# a list in a list using comphernsion  is nested   comprehension

# example:
matrix=[i for i in range(1,4)],[j for j in range(1,4)]
flat=[num for row in matrix for num in row ]
print(flat)

