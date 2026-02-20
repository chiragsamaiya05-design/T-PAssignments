def peakElement(lis):
    peak =[]
    for i in range(1,len(lis)):
        if lis[i-1]<lis[i] and lis[i+1]<lis[i]:
            peak.append(lis[i])
        
    return peak

ls = [1,2,3,5,4,9,7,8,6]

print(peakElement(ls))