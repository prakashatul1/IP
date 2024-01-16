# find the index if smallest element
def find_no_of_times(arr):

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = (start + end) // 2
        nexte = (mid + 1) % len(arr)
        previous = (mid + len(arr) - 1) % len(arr)

        if arr[mid] <= arr[nexte] and arr[mid] <= arr[previous]:
            return mid
        elif arr[start] <= arr[mid]:
            start = mid + 1
        elif arr[end] <= arr[end]:
            end = mid - 1

    return -1




