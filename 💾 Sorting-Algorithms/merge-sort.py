'''

— What is Merge Sort?

Merge sort may look intimidating when first learning about
it, but it is one of the fastest and efficient sorting algorithms.

— How does Merge Sort work?

Merge sort works by splitting the input list into two halves, 
repeating the process on those halves, and finally merging 
the two sorted halves together.

— When should I use this sorting algorithm?

Merge Sort is useful for sorting linked lists. Merge Sort 
is a stable sort which means that the same element in an 
array maintain their original positions with respect to 
each other

'''

def merge_sort(arr):
    length = len(arr)
    
    if length == 1:
        return arr
      
    mid_point = length // 2
    left_partition = merge_sort(arr[:mid_point])
    right_partition = merge_sort(arr[mid_point:])

    return merge(left_partition, right_partition)

def merge(left, right):
    output = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output
