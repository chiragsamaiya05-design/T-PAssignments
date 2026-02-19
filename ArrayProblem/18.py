# Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.

def movZeros(lis):
    for i in range(len(lis)):
       
        if lis[i]==0:
            
            lis.append(ls[i])
            lis[i]= -1

    lis = [x for x in lis if x != -1]
    return lis
        
 
        


ls = [10,0,0,1,2,3,4,5,60,0,0,0]

print(movZeros(ls))

