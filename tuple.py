        #   (                     tuple                               )
                #  are immutable sequences in Python, 
                # meaning that once a tuple is created, its elements cannot be changed, added, or removed.
                #  Tuples are defined by enclosing elements in parentheses `()`, 
                # and they can contain elements of different data types, including other tuples. 
                # They are often used to group related data together 
                # and can be used as keys in dictionaries due to their immutability.



# ============================
# # Reminder :

# a empty () would be a tuple 

# but a () with elements and no comma would not be consider as a tuple
# ===========================


# EXAMPLE:

names=('spiderman','Loki','scarlett johanson🫀','Ironman','Thor','hulk')


# ================
# Tuple packing:
#                 is when assing a element without using parentheses,
#                   Python automatically packs the values into a tuple.
# example:

t1=1,2,'spiderman',True
print(type(t1))



# ==========================
# Tuple unpacking
            # is when assaing a varaible with a tuple element
t2=1,2,'spiderman',True
a,b,c,d=t2
print(a)
print(b)

# -------------------------
# if there are many element assing it with a *
# but will be store in a form of list 

t3=1,2,'ironman',True
a,b,*c=t3


# ===============================




















































