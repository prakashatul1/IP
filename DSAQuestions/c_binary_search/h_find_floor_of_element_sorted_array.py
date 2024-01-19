def find_floor_element_sorted_array(arr, ele):

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = (start + end) // 2  # start + ((end - start)/2)
        if ele == arr[mid]:
            return mid
        elif ele < arr[mid]:
            end = mid - 1
        elif ele > arr[mid]:
            start = mid + 1
            res = arr[mid]

    return res


array1 = [5, 6, 7, 8, 9, 11]
print(find_floor_element_sorted_array(array1, 10))
