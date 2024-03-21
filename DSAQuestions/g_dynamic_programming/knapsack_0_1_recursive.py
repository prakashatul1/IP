"""
Maximum profit that can be achieved
"""
def knapsack(weight, value, w, n):
    # Base case: If no items left or no capacity in the knapsack
    if n == 0 or w == 0:
        return 0

    # If weight of the nth item is more than the knapsack capacity w,
    # then this item cannot be included in the optimal solution
    if weight[n - 1] > w:
        return knapsack(weight, value, w, n - 1)

    # Return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            value[n - 1] + knapsack(weight, value, w - weight[n - 1], n - 1),
            knapsack(weight, value, w, n - 1)
        )

# Test the function with the given weights and values
weight1 = [1, 2, 4, 7]
value1 = [2, 4, 5, 3]
n1 = 4
w1 = 7
print(knapsack(weight=weight1, value=value1, n=n1, w=w1))



weight1 = [1, 2, 4, 7]
value1 = [2, 4, 5, 3]
n1 = 4
w1 = 7
print(knapsack(weight=weight1, value=value1, n=n1, w=w1))
