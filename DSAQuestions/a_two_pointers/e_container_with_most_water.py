# https://leetcode.com/problems/container-with-most-water/description/
def maxArea(height) -> int:
    i, j = 0, len(height) - 1
    m = 0

    while i < j:

        h = min(height[i], height[j])
        w = j - i
        area = h * w
        m = max(m, area)

        if height[i] >= height[j]:
            j -= 1
        else:
            i += 1

    return m


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
