with open("ccopy.txt",'r') as f:
    data=f.read()
with open("ccopy1.txt",'w') as f:
    f.write(data)