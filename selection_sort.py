#Selection Sort

def selectionsort(arr):

  for i in range(0,len(arr)- 1):
    minn = i
    for j in range(i+1,len(arr)):
      if arr[j] < arr[minn]:
        minn = j
    arr[i],arr[minn] = arr[minn],arr[i]
  return arr

arr1 = [4,2,7,3]
print(selectionsort(arr1))
        
    
