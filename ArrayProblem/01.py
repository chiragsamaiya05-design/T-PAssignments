#Reverse an Array

ls = [1,2,3,4,5,6]
for i in ls:
    ls.pop(i)
    ls.append(i)

print(ls)  
