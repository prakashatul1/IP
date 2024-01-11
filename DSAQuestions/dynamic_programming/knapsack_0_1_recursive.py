"""
Maximum profit that can be achieved
"""


def knapsack(weight, value, w, n):
    if n == 0 or w == 0:
        return 0
    if weight[n - 1] <= w:
        return max(
            value[n - 1] + knapsack(weight, value, w - value[n - 1], n - 1),
            knapsack(weight, value, w, n - 1)
        )
    elif weight[n - 1] >= w:
        return knapsack(weight, value, w, n - 1)


weight1 = [1, 2, 4, 7]
value1 = [2, 4, 5, 3]
n1 = 4
w1 = 7
print(knapsack(weight=weight1, value=value1, n=n1, w=w1))
