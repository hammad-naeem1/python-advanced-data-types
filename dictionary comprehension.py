                    # (      Dictionary    comphersion               )

        # Python dictionary comprehension provides a concise,
        # one-line syntax to create new dictionaries from any iterable


# example :
names=['spiderman','Loki','scarlett johanson🫀','Ironman','Thor','hulk']
length={w:len(w) for w in names}
for key,value in length.items():
    print(f" key : {key}  value : {value}")



# example 2 
nums=[i for i in range(1,10)]
even_num_square={n:n * n for n in nums if n%2==0 }
for key,value in even_num_square.items():
    print(f" key : {key}  value : {value}")



     