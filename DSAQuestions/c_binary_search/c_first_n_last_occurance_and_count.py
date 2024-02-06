def first_occurrence(arr, ele):
    start = 0
    end = len(arr) - 1
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
    start = 0
    end = len(arr) - 1
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


def find_count(arr, ele):
    first = first_occurrence(arr, ele)
    last = last_occurrence(arr, ele)

    return last - first + 1
