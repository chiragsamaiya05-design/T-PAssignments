def mergeSorted(arr1, arr2):
    i = 0
    j = 0
    L1= len(arr1)
    L2 = len(arr2)
    merArr = []

    while i < L1 and j < L2:
        if arr1[i] < arr2[j]:
            merArr.append(arr1[i])
            i += 1
        else:
            merArr.append(arr2[j])
            j += 1

    while i<L1:
        merArr.append(arr1[i])
        i+=1

    while j < L2:
        merArr.append(arr2[j])
        j+=1

    return merArr

ls1 =[1,2,3,5]
ls2 =[1,7,8,9]

print(mergeSorted(ls1,ls2))