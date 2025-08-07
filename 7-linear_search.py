#Linear search

def linearsearch(arr,k):
  for i in range(0,len(arr)):
    if arr[i] == k:
      return "element found"
  return "element not found"
  
