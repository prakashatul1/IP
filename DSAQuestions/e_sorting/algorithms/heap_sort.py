import heapq


def heap_sort(arr):
    # Create a min-heap from the array
    heapq.heapify(arr)

    # Repeatedly remove the smallest element from the heap and add it to the result array
    sorted_array = [heapq.heappop(arr) for _ in range(len(arr))]
    return sorted_array


# Example usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print("Sorted array:", sorted_arr)
