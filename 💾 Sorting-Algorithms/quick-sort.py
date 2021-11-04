'''
— What is Quick Sort?

Quick sort is a highly efficient sorting algorithm 
and is based on partitioning of array of data into smaller arrays.

— How does Quick Sort work?

Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element
from the array and partitioning the other elements into two sub-arrays, according to
whether they are less than or greater than the pivot. For this reason, it is 
sometimes called partition-exchange sort.

— When should I use this sorting algorithm?

So, to generalize, quicksort is probably more effective for datasets that fit in memory. 
For stuff that's larger, it's better to use mergesort. The other 
general time to use mergesort over quicksort is if the data is very similar

'''

def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1
  for j in range(low, high):
    if arr[j] <= pivot:
      i = i + 1

      (arr[i], arr[j]) = (arr[j], arr[i])
  (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

  return i + 1

def quickSort(arr, low, high):
  low = 0
  high = len(arr)
  if low < high:
    pi = partition(arr, low, high)
    quickSort(arr, low, pi - 1)
    quickSort(arr, pi + 1, high)
