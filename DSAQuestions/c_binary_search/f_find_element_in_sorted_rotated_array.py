def find_element_index(arr, ele):
    n = find_no_of_times_array_rotated(arr)
    print(f'mid : {n}')
    end = len(arr) - 1
    start = 0

    if ele == arr[n]:
        return n
    elif ele > arr[end]:
        return binary_search(arr, start, n - 1, ele)
    else:
        return binary_search(arr, n + 1, end, ele)


def find_no_of_times_array_rotated(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = (start + end) // 2
        nxt = (mid + 1) % len(arr)
        previous = (mid + len(arr) - 1) % len(arr)

        if arr[mid] <= arr[nxt] and arr[mid] <= arr[previous]:
            return mid
        elif arr[nxt] < arr[mid]:
            start = mid + 1
        elif arr[previous] < arr[mid]:
            end = mid - 1

    return 0


def binary_search(arr, start, end, ele):
    while start <= end:

        mid = (start + end) // 2
        print(mid, start, end)
        if ele == arr[mid]:
            return mid
        elif ele < arr[mid]:
            end = mid - 1
        elif ele > arr[mid]:
            start = mid + 1

    return -1


array1 = [10, 17, 1, 3, 4, 4, 5, 7]
element1 = 10

array2 = [15, 16, 17, 1, 2, 3, 4]
element2 = 2

print(find_element_index(array2, element2))
