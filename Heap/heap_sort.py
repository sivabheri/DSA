def heapify(arr, n, i):
    largest = i  
    left = 2 * i + 1  
    right = 2 * i + 2  
    
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  

def heap_sort(arr):
    n = len(arr)

    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)  

# Example usage
arr = [3, 1, 4, 1, 5, -2, -3, 0]
heap_sort(arr)
print("Sorted array:", arr)  # Output: Sorted array: [-3, -2, 0, 1, 1, 3, 4, 5]