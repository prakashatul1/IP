# https://leetcode.com/problems/n-th-tribonacci-number/description/

"""
Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

"""


def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n <= 2:
        return 1

    new = 0
    zero = 0
    first = 1
    second = 1

    for i in range(3, n + 1):
        new = zero + first + second
        zero, first, second = first, second, new

    return new


print(tribonacci(n=25))  # result  =  1389537
