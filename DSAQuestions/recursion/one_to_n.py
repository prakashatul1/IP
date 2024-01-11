def print_n_to_1(n):
    if n < 1:
        return
    print(n, end=' ')
    print_n_to_1(n - 1)

def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n, end=' ')

# Example usage
n = 5
print("n to 1:")
print_n_to_1(n)
print("\n1 to n:")
print_1_to_n(n)
