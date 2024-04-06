# find the index if minimum value element
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
def find_no_of_times(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = (start + end) // 2
        nexte = (mid + 1) % len(arr)
        previous = (mid + len(arr) - 1) % len(arr)

        if arr[mid] <= arr[nexte] and arr[mid] <= arr[previous]:
            return arr[mid]
        elif arr[start] < arr[end]:
            return arr[start]
        elif arr[start] <= arr[mid]:
            start = mid + 1
        else:
            end = mid - 1


print(find_no_of_times([2, 1]))
