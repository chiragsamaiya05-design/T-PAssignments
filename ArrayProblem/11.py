def findNum(lis,x):

    if x in lis:
        lis.remove(x)
    return lis

ls = [6,5,8,9,1,100,2,3]

print(findNum(ls,100))