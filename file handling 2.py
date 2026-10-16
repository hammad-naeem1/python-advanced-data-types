\
#   (    how to read a file ?   )

# use (r) to read from a file :

files=open('test.csv','r')
content=files.read()
# print(content)

for i in content:
    print(i.sort())