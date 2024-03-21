def knapsack(weight, value, w, n):
    # Initialize a 2D array 't' with 0 for the first row and column
    t = [[0 if i == 0 or j == 0 else None for j in range(w + 1)] for i in range(n + 1)]

    # Fill the rest of the table bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if weight[i - 1] <= j:
                t[i][j] = max(value[i - 1] + t[i - 1][j - weight[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]

    return t[n][w]


# Test the function with the given weights and values
weight1 = [1, 2, 4, 7]
value1 = [2, 4, 5, 3]
n1 = 4
w1 = 7
print(knapsack(weight=weight1, value=value1, n=n1, w=w1))
