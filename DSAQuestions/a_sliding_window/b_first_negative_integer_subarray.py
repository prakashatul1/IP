from collections import deque


def find_negative_subarray(array_int: list[int], k: int) -> list[int]:
    i, j = 0, 0
    length = len(array_int)
    calc_list = []
    result = []

    while j < length:

        # calculation in cache
        if array_int[j] < 0:
            calc_list.append(array_int[j])

        # increasing window till size k
        if j - i + 1 < k:
            j += 1

        # when window is of size k
        elif j - i + 1 == k:

            # result for the window
            if len(calc_list) == 0:
                result.append(0)
            else:
                result.append(calc_list[0])

                # adjust the calculation cache to work with next
                # window before increasing i
                if array_int[i] == calc_list[0]:
                    calc_list.pop(0)

            j += 1
            i += 1

    return result


array1 = [12, -1, -7, 8, -15, 30, 16, 23]
print(find_negative_subarray(array1, 3))
