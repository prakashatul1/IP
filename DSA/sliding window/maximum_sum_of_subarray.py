def find_max(array_int: list[int], k: int) -> int:
    j, i = 0, 0
    ms = 0
    summ = 0
    length = len(array_int)

    while j < length:

        # calculation in cache
        summ = summ + array_int[j]

        # increasing window till size k
        if (j - i + 1) < k:
            j += 1

        # when window is of size k
        elif (j - i + 1) == k:

            # result for the window
            ms = max(ms, summ)

            # adjust the calculation cache to work with next
            # window before increasing i
            summ = summ - array_int[i]

            j += 1
            i += 1

    return ms


array1 = [1, 2, 3, 2, 1, 7, 10, 2, 3]
print(find_max(array1, 3))
