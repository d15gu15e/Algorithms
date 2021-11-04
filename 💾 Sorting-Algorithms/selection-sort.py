'''

— What is Selection Sort?
Selection sort is a simple sorting algorithm. This sorting algorithm
uses in-place comparison to divide the list into two sections:
sorted items on the left and unsorted items on the right. The
sorted section begins with an empty list, while the unsorted section
contains the entire list.

— How does Selection Sort work?

The selection sort algorithm sorts an array by repeatedly finding the 
minimum element (considering ascending order) from unsorted part and
putting it at the beginning.

— When should I use this sorting algorithm?

Selection sort can be good at checking if everything is already sorted.
It is also good to use when memory space is limited. This is because 
unlike other sorting algorithms, selection sort doesn't go around
swapping things until the very end, resulting in less temporary storage space used.

'''

def selectionSort(arr):
    for i in range(len(arr) - 1):
        # Get smallest element in unordered subarray
        n = min(arr[i:])
        # Place smallest element in ordered subarray
        arr[i], arr[n] = arr[n], arr[i]
    return arr
