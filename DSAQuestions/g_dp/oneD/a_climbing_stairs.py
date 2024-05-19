# https://leetcode.com/problems/climbing-stairs/description/
"""
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


# dp
def climbStairs(n):
    if n <= 3:
        return n
    n1, n2 = 2, 3

    for i in range(4, n + 1):
        temp = n1 + n2
        n1 = n2
        n2 = temp
    return n2


def climb_stairs(n):
    # Memoization dictionary
    memo = {}

    def climb(remaining):
        # If no steps left, we are at the top
        if remaining == 0:
            return 1
        # If negative steps, it's not a valid path
        if remaining < 0:
            return 0
        # Check if the result is already computed
        if remaining in memo:
            return memo[remaining]

        # Recursively calculate the number of ways to reach the top
        # by taking 1 step or 2 steps
        ways = climb(remaining - 1) + climb(remaining - 2)

        # Store the result in the memoization dictionary
        memo[remaining] = ways
        return ways

    # Start the recursion from n steps
    return climb(n)


# Example usage
print(climb_stairs(2))  # Output: 2
print(climb_stairs(3))  # Output: 3
print(climbStairs(2))
print(climbStairs(3))

