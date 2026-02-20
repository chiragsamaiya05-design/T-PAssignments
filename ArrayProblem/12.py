def MissNum(lis):
    n = len(lis)+1
    sumOfN = n*(n+1)//2
    sum = 0
    for i in lis:
        sum +=i

    if sumOfN != sum:
        return (sumOfN - sum)
    
ls = [1,2,3,4,5,6,8,9]

print(MissNum(ls))