def find_duplicates_and_missing_numbers(arr):
    n = len(arr)
    duplicates = []
    missing = []

    # Mark duplicates
    for i in range(n):
        index = abs(arr[i]) - 1
        if arr[index] < 0:
            duplicates.append(index + 1)
        else:
            arr[index] = -arr[index]

    # Find missing numbers
    for i in range(n):
        if arr[i] > 0:
            missing.append(i + 1)

    return duplicates, missing

# Test the function
input_array = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates_and_missing_numbers(input_array))
