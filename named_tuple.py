from collections import namedtuple

employe=namedtuple('employe',['id','name','salary'])

employe1=employe(1,'hammad',56000)
employe2=employe(2,"barahjan",89011)
print(f"id:{employe1.id}  name:{employe1.name}")
print(employe2)
# ===============================
# replaing a value in namedtuple
new_employe1=employe1._replace(salary=7807)

# -------------------------------------
# turing a list to namedtuple
s1=[3,'jaleel',9022]
s1=employe._make(s1)
print(s1)

# -------------------------------------------
# turing a namedtuple to dictinary 
d1=new_employe1._asdict()
print(d1)
for key,value in d1.items():
    print(f"key:{key}  and value:{value}")

    
