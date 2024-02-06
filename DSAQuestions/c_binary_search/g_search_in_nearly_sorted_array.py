def search_in_nearly_sorted_array(arr, ele):
    # Initialize start and end indices.
    start = 0
    end = len(arr) - 1

    # Continue searching while the start index is less than or equal to the end index.
    while start <= end:
        # Calculate the mid index.
        mid = start + ((end - start) // 2)

        # Check if the element is at the mid index.
        if ele == arr[mid]:
            return mid
        # If not, check the element to the left of mid, ensuring mid is not the first element.
        elif mid >= start and arr[mid - 1] == ele:
            return mid - 1
        # Then, check the element to the right of mid, ensuring mid is not the last element.
        elif mid <= end and arr[mid + 1] == ele:
            return mid + 1
        # If the element is less than that at mid, adjust the end index to two positions left of mid.
        elif ele < arr[mid]:
            end = mid - 2
        # If the element is greater than that at mid, adjust the start index to two positions right of mid.
        elif ele > arr[mid]:
            start = mid + 2
    # If the element is not found, the function implicitly returns None.


array1 = [5, 6, 7, 8, 10, 9]  # Example of a nearly sorted array.
print(search_in_nearly_sorted_array(array1, 9))  # Searches for the element 9.
