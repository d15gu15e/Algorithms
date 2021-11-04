'''

— What is Insertion Sort?

Insertion Sort is very similar to Bubble Sort, but guarantees one major
thing, insertion sort will *always* return a sorted list in one iteration.

— How does Insertion Sort work?

The values are compared in order, starting with the second item in the list.
No adjustments are done if this value is bigger than the value to its left.
Otherwise, this value is repeatedly shifted to the left until it meets a smaller value. 
After that, the sorting process starts over with the next value.

— When should I use this sorting algorithm?

Insertion sort is used when number of elements is small. 
It can also be useful when input array is almost sorted, 
only few elements are misplaced in complete big array.

'''

def insertionSort(arr):
    # We start from 1 since the first element doesn't have a neighbor to the left
    for i in range(1, len(arr)):
        n = arr[i]
        while i > 0 and arr[i - 1] > n:
            arr[i] = arr[i -1]
            i = i - 1
        arr[i] = n
    return arr
