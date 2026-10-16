
# there is only 2 types of files are there :
      # (    binary file           )   and       (    text files             )

# text_file:
            # human readable :

# binary files:
            # computer readable
# ------------------------------------------


#           how to open a file using      (    with   )

with open('test.txt','r') as file:
    content=file.read()
    print(content)







# #               ( to open a file we use open()  )

# file_read=open('test.txt','w')
# file_read.write('hello how are you \n')
# file_read.write('iam good')

# #        after opening you must close the file:
# file_read.close()
 
# # ========================================================

#           # (  if you want to write a whole list use ( writelines ) :) 

# file_read=open('test.txt','w')
# l1=['1 apple\n','2 banana\n','3 mango\n']
# file_read.writelines(l1)
# file_read.close()
# # =====================================

# #           (use append to write in a file without removing the previous one)


# # we will use (a) instead of  w means write
# file_read=open('test.txt','a')
# l1=['1 apple\n','2 banana\n','3 mango\n']
# file_read.write('above are the fruits :')
# file_read.close()





















