import heapq

def mergeKArrays(arrays):
    min_heap = []
    result = []

    for i in range(len(arrays)):
        if arrays[i]:
            heapq.heappush(min_heap, (arrays[i][0], i, 0))

    while min_heap:
        value, array_index, element_index = heapq.heappop(min_heap)
        result.append(value)

        if element_index + 1 < len(arrays[array_index]):
            next_value = arrays[array_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, array_index, element_index + 1))

    return result

arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
merged_array = mergeKArrays(arrays)
print("Merged array is:", merged_array)