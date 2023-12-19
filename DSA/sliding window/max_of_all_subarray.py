from collections import deque


def find_max_subarray(array_int: list[int], k: int) -> list[int]:
    i, j = 0, 0
    length = len(array_int)
    l = deque()
    result = []

    while j < length:

        # calculation in cache
        if (len(l) == 0) or (l[0] > array_int[j]):
            l.append(array_int[j])
        elif l[0] < array_int[j]:
            l.appendleft(array_int[j])

        # increasing window till size k
        if j - i + 1 < k:
            j += 1

        # when window is of size k
        elif j - i + 1 == k:

            # result for the window
            result.append(l[0])

            # adjust the calculation cache to work with next
            # window before increasing i
            if array_int[i] == l[0]:
                l.popleft()

            j += 1
            i += 1

    return result


array1 = [3, 1, -1, -2, 5, 3, 6, 7]
print(find_max_subarray(array1, 3))
