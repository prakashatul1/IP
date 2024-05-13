from collections import deque
import heapq


def kth_largest_in_windows(arr, m, k):
    n = len(arr)
    i, j = 0, 0
    subarray = []
    heap = []
    temp = None
    while j < n:

        subarray.append(-arr[j])
        # if len(heap) >= m:
        #     heapq.heappop(heap)
        # heapq.heappush(heap, arr[j])

        if len(subarray) == m:
            temp = arr[i]
            heapq.heapify(subarray)
            print(-subarray[0])

        elif len(subarray) > m:
            i += 1
            subarray.remove(-temp)

            if len(subarray) == m:
                temp = arr[i]
                heapq.heapify(subarray)
                print(-subarray[0])

        j += 1


arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
m = 3
print(kth_largest_in_windows(arr, k, m))  # Output: [3, 3, 5, 5, 6, 7]
