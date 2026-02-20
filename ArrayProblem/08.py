def findSum(arr,tar):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[i]+arr[j]==tar:
                return arr[i],arr[j]
            
ls = [1,2,3,4,6,8,9,0]
print(findSum(ls,5))
