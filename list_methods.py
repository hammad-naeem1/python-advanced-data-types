# === modifying a list =========

# example of modifying a lists:
my_list=['ironman',7,18]

# adding a value in a list 
my_list.append('spiderman')
print(my_list)
Reply

# =========================
# adding a value in a list  with given position
# ============
my_list.insert(1,'keyboard')
print(my_list)

# ============================
# removing something from a list
# ==========
my_list.remove('ironman')
print(my_list)

#  remove method wil only remove the first element
#  the remove method will find starting from 0 index

# ===

my_list.pop()
print(my_list.pop())
# pop will remove the last element from the list if index is not given ! 
#we can store the pop in a variable and it return the removed last value

# if index is given :
# it would remove the element and will return that element
my_list.pop()
print(my_list.pop(1))

# ==============================================================================


# ================
# Replacing something in a list
# =====

my_list[1]=10
print(my_list)

# it replces a value with his index 
# =======================================





