def LeaderElem(lis):
    max_right = -1
    leader =[]
    for i in range(1,len(lis)):
        
        if lis[i]>max_right:

            leader.append(lis[i])
            max_right=lis[i]
            
    return leader

ls = [16,17,4,3,5,2]

print(LeaderElem(ls))
