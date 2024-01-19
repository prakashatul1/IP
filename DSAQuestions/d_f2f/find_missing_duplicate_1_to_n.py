def find_missing_and_duplicate(arr):
    n = len(arr)
    duplicate = missing = -1

    # Place each number in its correct position
    for i in range(n):
        while arr[i] != i + 1:
            # If the correct position already has the same number, it's the duplicate
            if arr[arr[i] - 1] == arr[i]:
                duplicate = arr[i]
                break
            # Swap the elements
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            print(arr)

    # Find the missing number
    for i in range(n):
        if arr[i] != i + 1:
            missing = i + 1
            break

    return [duplicate, missing]

# Test the function
input_array = [3, 1, 2, 5, 3]
print(find_missing_and_duplicate(input_array))
