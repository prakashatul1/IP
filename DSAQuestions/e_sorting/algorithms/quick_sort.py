import random


def quick_sort(arr):
    helper(arr, 0, len(arr) - 1)
    return arr


def helper(arr, start, end):
    # leaf worker
    if start >= end:
        return

    # # randomised vs deterministic
    pivot = random.randint(start, end)
    print(pivot)
    arr[pivot], arr[start] = arr[start], arr[pivot]

    # Lomuto's partitioning
    # smaller = partition_lomuto(arr, start, end)

    # hoare's partitioning
    smaller = partition_hoare(arr, start, end)

    # internal worker
    helper(arr, start, smaller - 1)
    helper(arr, smaller + 1, end)


def partition_lomuto(arr, start, end):
    smaller = start

    for bigger in range(start + 1, end + 1):
        if arr[bigger] < arr[start]:
            smaller += 1
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]

    arr[start], arr[smaller] = arr[smaller], arr[start]
    return smaller


def partition_hoare(arr, start, end):
    smaller = start + 1
    bigger = end

    while smaller <= bigger:
        if arr[smaller] < arr[start]:
            smaller += 1
        elif arr[bigger] > arr[start]:
            bigger -= 1
        else:
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
            smaller += 1
            bigger -= 1

    arr[start], arr[bigger] = arr[bigger], arr[start]
    return bigger


print(quick_sort([5, 8, 3, 9, 4, 1, 7]))
