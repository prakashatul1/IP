def push_zeroes_to_right(arr):
    n = len(arr)
    pos = 0  # Pointer to place the next non-zero element

    # Traverse the array
    for i in range(n):
        if arr[i] != 0:
            # Swap the non-zero element with the element at 'pos'
            arr[i], arr[pos] = arr[pos], arr[i]
            pos += 1  # Move the 'pos' pointer to the next position

    return arr

# Example usage
array = [0, 2, 0, 3, 0, 10, 6]
push_zeroes_to_right(array)
print(array)
