def findLengthOfShortestSubarray(arr):
    n = len(arr)

    i, j = 0, n - 1

    while i + 1 < n and arr[i + 1] >= arr[i]:
        i += 1

    if i == n - 1:
        return 0

    while j >= 0 and arr[j - 1] <= arr[j]:
        j -= 1

    ans = min(n, n - i - 1, j)

    for l in range(i + 1):
        r = j
        while r < n and arr[r] < arr[l]:
            r += 1
        ans = min(ans, r - l - 1)

    return ans


arr1 = [1, 6, 7, 9, 12, 5, 6, 10, 11, 15]
print(findLengthOfShortestSubarray(arr1))
