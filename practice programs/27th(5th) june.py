def print_inverted_pyramid(rows):
    # Outer loop for rows
    for i in range(rows, 0, -1):
        # Inner loop for columns
        for j in range(rows - i):
            print(' ', end='')
        for j in range(2 * i - 1):
            print('*', end='')
        print()

# Example usage:
rows = int(input("Enter the number of rows: "))
print_inverted_pyramid(rows)
