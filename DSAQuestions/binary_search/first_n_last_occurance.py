def first_occurrence(arr, ele):
    l: int = len(arr)
    start = 0
    end = l - 1
    res = -1

    while start <= end:

        mid = start + end // 2  # start + ((end - start)/2)
        if ele == arr[mid]:
            res = mid
            end = mid - 1
        elif ele < arr[mid]:
            end = mid - 1
        elif ele > arr[mid]:
            start = mid + 1

    return res


def last_occurrence(arr, ele):
    l: int = len(arr)
    start = 0
    end = l - 1
    res = -1

    while start <= end:

        mid = start + end // 2  # start + ((end - start)/2)
        if ele == arr[mid]:
            res = mid
            start = mid + 1
        elif ele < arr[mid]:
            end = mid - 1
        elif ele > arr[mid]:
            start = mid + 1

    return res
