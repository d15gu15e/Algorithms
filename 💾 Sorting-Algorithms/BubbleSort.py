def bubbleSort(arr):
    # Go through every item in the list
    for i in range(len(arr)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                # Swap the elements if they are not in the right order.
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
