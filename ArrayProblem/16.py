def sortedArrays(arr1,arr2):
  if len(arr1) != len(arr2):
        return False
  freq ={}

  for num in arr1:
      freq[num]= freq.get(num, 0) + 1
    
  for num in arr2:
      if num not in freq or freq[num] == 0:
          return False
      
  return True



ls1 =[1,2,3,4]
ls2 =[4,3,2,5]

print(sortedArrays(ls1,ls2))