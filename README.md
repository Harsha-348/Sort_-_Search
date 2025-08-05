# Sorting & Searching

# Sorts: 
     1.Bubble sort
     2. --
     3. --
     4. -- 
     5. -- 
        

-----------------------------------------------------------------( Bubble sort )------------------------------------------------

# 1.Bubble sort
- It is a simplest sorting algorithm in which it performs by comparing and swapping the adjacent elements in an array.
- It is only suitable for small data sets and not for large data sets.

# Complexities:
 - Time complexity: O(n²)      - (nested loops usage)
 - Space complexity: O(1)      - (No extra space used)

# Steps to perform:
1. Outer Loop (i):

Runs n times (where n = len(arr)), ensuring all elements are processed.

2. Inner Loop (j):

Goes from 0 to n-i-1 because after each pass, the largest unsorted element "bubbles up" to its correct position at the end.

3. Swap Condition:

If arr[j] > arr[j+1], the elements are swapped, moving the larger element towards the end.

3. Return Statement:

Returns the sorted array (though Bubble Sort is typically in-place, meaning it modifies the original array).



---------------------------------------------------------------------(  sort )-------------------------------------------------
---------------------------------------------------------------------(  sort )-------------------------------------------------
---------------------------------------------------------------------(  sort )-------------------------------------------------
---------------------------------------------------------------------(  sort )-------------------------------------------------



-------------------------------------------------------------------------------------------------------------------------------

# Searching algorithms

Searching algorithms are mainly used to find the location of an element in an array.
There are two types in the searching algo:
               1. Linear search
               2. Binary search
               
----------------------------------------------------------------( Linear search )----------------------------------------------

- It is mainly used on unsorted array.
- It does one by one element comparision of the element with the given array elements.
- It is faster when the element is in the first or second index but what if the element is present at the end of the array.

     - Time complexity is O(n)   
     - Space complexity is O(1)

 
-----------------------------------------------------( Binary search )--------------------------------------------

- It is used on the sorted array.
- It is fast than the linear search.
- In Binary search, we will find the middle element and divide array in to by lower and upper bounds till the element is found.

     - Time complexity is O(log n)
     - space complexity is O(1)
 
  



