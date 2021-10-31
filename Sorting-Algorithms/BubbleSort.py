'''

— How does Bubble Sort work?

Bubble Sort is one of the easiest to understand algorithms:
Start from the leftmost element, compare it to the neighboring
element to the right, and put them in the correct order. 

— When should I use this sorting algorithm?

Honestly? Never. With an average complexity of О(n²), it's incredibly
slow, especially when handling a lot of data.

'''

def bubbleSort(arr):
    # Go through every item in the list
    for i in range(len(arr)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                # Swap the elements if they are not in the right order.
                arr[j], arr[j+1] = arr[j+1], arr[j]
