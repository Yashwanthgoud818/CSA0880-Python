def print_hollow_square(rows):
    for i in range(rows):
        for j in range(rows):
            if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
                print('$', end=' ')
            else:
                print(' ', end=' ')
        print()

# Example usage for hollow square dollar pattern:
rows = int(input("Enter number of rows for hollow square dollar pattern: "))
print("Hollow Square Dollar Pattern:")
print_hollow_square(rows)
