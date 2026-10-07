#          (                     set                                  )

                # a set in python is a collection of unique elements. 
                # It is an unordered data structure that allows for efficient membership
                # testing, addition, and removal of elements.
                # Sets are defined using curly braces {} or the set() constructor.
                
# example :

names={'spiderman','Loki','scarlett johanson🫀','Ironman','Thor','hulk'}


#reminder :
        # sets never allow duplicate element or value 


# ===============================================================

                # (frozenset)
#               is a method to make a set which is immutable 
s1={1,2,5,6,}
new_s1=frozenset(s1)
print(s1)










# ===================================

# adding in set :
# example 

                        #    .add()    
# adds element in a last of a set 

names.add('ironman')

print(names)

# =================================

# removing a element in a set 
# --------------------
                            # .remove()
# it removes a elemrnt from a set but gives error if the element not presesnt 

# names.remove('captain america')


# ==========================
                            # .discard()
# its also use to remove a elemrnt from a set but not give ant  error if the element not presesnt\

names.discard('captain america')

# ===========================================


















































