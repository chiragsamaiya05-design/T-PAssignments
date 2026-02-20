def Duplicates(lis):
    i = 1
    while i < len(lis):
        if lis[i] == lis[i-1]:
            lis.pop(i)
        else:
            i += 1
    return lis

ls = [1,2,2,3,3,4,5,6]
print(Duplicates(ls))

