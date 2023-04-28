list1=["gadha", "ullu", "jatayu",]
with open("censoredlist.txt",'r') as y:
    data=y.read()
for z in list1:
    data=data.replace(z,"@#$%&*")
with open("censoredlist.txt",'w') as y:
    data=y.write(data)       