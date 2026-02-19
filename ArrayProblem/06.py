
def isSorted(lis):
    for i in range(1,len(lis)):
        if lis[i]<lis[i-1]:
            return False
    return True

ls1 = [6,5,8,9,1,100,2,3]

ls2 = [1,2,3,5,6,7,9]

print(isSorted(ls1))

print(isSorted(ls2))