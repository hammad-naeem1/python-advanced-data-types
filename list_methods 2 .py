# ==================

items=['ironman','spiderman',9,True]
items2=[9,6,0,5,6]

# ================

# sort()
# --
# it sort the elements in a list in ascending order

items2.sort()
print(items2)
# -----------------
# if you will use reverse it would sort them in descending order 
items2.sort(reverse=True)
print(items2)

# -------------------

# =============================================================
#                 (     sorted():              )
# s a function which returns a new list sorting the elements of a list givenn as parametre
sorted_list=sorted(items2)
print(sorted_list)
# =======================

# ============================================
#          reverse:
# it reverses the order of the elements in a list
sorted_list.reverse()
print(sorted_list)

# # ==================

# ===========================================
#    (      index                 )     

# index methods return the position in a list 
print(items.index('spiderman'))


# ================

# count:
# it returns how many time a element appers

print(items.count('ironman'))

# ===============
        #   (     # extend:          )
#     it adds the elements of a list to another list
# items.extend(items2)
# print(items)



