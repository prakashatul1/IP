def search_in_nearly_sorted_array(arr, ele):
    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = start + ((end - start) // 2)
        if ele == arr[mid]:
            return mid
        elif mid >= start and arr[mid - 1] == ele:
            return mid - 1
        elif mid <= end and arr[mid + 1] == ele:
            return mid + 1
        elif ele < arr[mid]:
            end = mid - 2
        elif ele > arr[mid]:
            start = mid + 2


array1 = [5, 6, 7, 8, 10 , 9]
print(search_in_nearly_sorted_array(array1, 9))
