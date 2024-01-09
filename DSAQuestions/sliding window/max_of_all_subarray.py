from collections import deque


def find_max_subarray(array_int: list[int], k: int) -> list[int]:
    i, j = 0, 0
    length = len(array_int)
    l = deque()
    result = []

    while j < length:

        """
        remove element from deque from right if current element in loop
        is greater than smallest element in deque in the right
        """
        while l and array_int[j] > l[-1]:
            l.pop()

        # calculation in deque
        # add every element to deque
        # eg : 5, 4, 3
        l.append(array_int[j])


        # increasing window till size by 1
        if j - i + 1 < k:
            j += 1

        # if window is of size k
        elif j - i + 1 == k:

            # result for the window
            result.append(l[0])

            # adjust the calculation cache to work with next
            # window before increasing i
            # basically removing element from left of deque
            # since it has maximum element after each window calculation
            if array_int[i] == l[0]:
                l.popleft()

            j += 1
            i += 1

    return result


# array1 = [3, 1, -1, -2, 5, 3, 6, 7]
array1 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
array1 = [1,3,-1,-3,5,3,6,7]
array1 = [1,3,1,2,0,5]
array1 = [-7,-8,7,5,7,1,6,0]

print(find_max_subarray(array1, 3))
