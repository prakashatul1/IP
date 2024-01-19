def find_max_circular(array_int, k):
    j, i = 0, 0
    ms = 0
    summ = 0
    length = len(array_int)

    while j < 2 * length:  # Loop over the array twice

        # Use modulo operation to wrap around the array
        index = j % length
        summ += array_int[index]

        # Increase window size until it reaches size k
        if (j - i + 1) < k:
            j += 1
        elif (j - i + 1) == k:
            ms = max(ms, summ)
            # Subtract the element at the start of the window and slide the window
            summ -= array_int[i % length]
            i += 1
            j += 1

    return ms

# Test the function
array1 = [1, 2, 3, 2, 1, 7, 10, 2, 3]
print(find_max_circular(array1, 3))
