def majorityEle(lis):
    freq = {}

    for num in lis:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for key in freq:
        if freq[key]>len(lis)//2:
            return key
        
    return None
        
ls = [ 0,0,0,5,5,5,5,5,5,5,4,5,5,5,2,3,4]

print(majorityEle(ls))