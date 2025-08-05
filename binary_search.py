# Binary search

def binarysearch(self, arr, k):
        
        low = 0
        high = len(arr) - 1
        result = -1
        
        for i in range(0,len(arr)):
            
            mid = low + (high - low) // 2
            
            if arr[mid] == k:
                result = mid
                high = mid - 1
            
            elif arr[mid] < k:
                low  = mid + 1
            else:
                high = mid - 1
        
        return result
                
