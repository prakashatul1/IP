def binary_search(arr, ele):
    l = len(arr)
    left = 0
    right = l - 1

    while left <= right:

        mid = left + right // 2  # start + ((end - start)/2)
        if ele == arr[mid]:
            return mid
        elif ele < arr[mid]:
            right = mid - 1
        elif ele > arr[mid]:
            left = mid + 1

    return -1
