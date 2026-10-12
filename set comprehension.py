                #  (     # set  comprehension          )

    # a concise, single-line syntax used to create new lists from existing iterables. 
    # Ierate at allows you to gen new list by applying an expression to each item in an 
    # iterable, optionally filtering items based on a condition.

        #    (1)what to kepp   (2) for each item   (3)in collection





# example :
s1={i*i for i in range(1,10) }
print(s1)

names=['spiderman','Loki','scarlett johanson🫀','Ironman','Thor','hulk']
s2={len(i)for i in names}
print(s2)