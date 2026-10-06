#   ======== lists  =============
# list can store multiple values in a single variable.
# list are ordered 
# list are mutaible
# list allow duplicate values

# example :
list=['ironman',7,True,20.7,'spiderman','keyboard',False]  

# ===
# acessinng a list
print(list)
# ===
# indexing in lists
print(list[1])
# negative indexing 
print(list[-1])

# -------------
# slicing in list
# ==
print(list[0:])
print(list[1:4])
print(list[:3])
print(list[1:5:2])
print(list[::2])
print(list[::-1])
print(list[-1:-4:-1])

# =============================================

# =======
# lopping through a list 
# ========
# step_1 of lopping
for i in range(len(list)):
    print(list[i])

# step 2 of lopping
for list_elements in list:
    print(list_elements,end=" - ")

#  if you want index and item both then use enumerate function
for index,item in enumerate(list):
    print(f"index is {index} and item is {item}",end='')



# =======p
# lopping through a list 
# ========
# step_1 of lopping
for i in range(len(list)):
    print(list[i])

# step 2 of lopping
for list_elements in list:
    print(list_elements,end=" - ")




# list constuctor 
# example :
type=list("spiderman")
# it converts most of type to list even strings
print(type)
for list_elements in type:
    print(list_elements,end=" ")





































