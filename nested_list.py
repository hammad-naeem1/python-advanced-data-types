
# nested list 

    # it is a list containg another list init useful for metrices ,grids and records

# example

list_1=[12,[True,False,34],45,[67,89,90],['ironman','spiderman']]
print(list_1[-1])




# ===========
# a list to variables in a single statement is called list unpacking

# example :# list unpacking
        # assigning the values of 
point=[10,20,30]
x,y,z=point
print(x,y,z)\

    # if there is more than element in list your asing you can just use
point=[10,20,30,50,89]
x,y,*z=point
print(x,y,z)