def maxTurbulenceSize(arr) -> int:
    l, r = 0, 1
    res, prev = 1, ""

    while r < len(arr):
        if arr[r - 1] > arr[r] and prev != ">":
            res = max(res, r - l + 1)
            r += 1
            prev = ">"
        elif arr[r - 1] < arr[r] and prev != "<":
            res = max(res, r - l + 1)
            r += 1
            prev = "<"
        else:
            r = r + 1 if arr[r] == arr[r - 1] else r
            l = r - 1
            prev = ""
    return res


print(maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
# 9 > 4 > 2 < 10 > 7 < 8 = 8 > 1 < 9
# result = 5
