def print_numbers(M, N, K):
    current = M
    while current <= N:
        print(current)
        current += K + 1

# Sample Input
M = 50
N = 100
K = 7

# Print the numbers
print_numbers(M, N, K)
