def print_square_star(rows):
    print("Square Star Pattern:")
    for i in range(rows):
        print('* ' * rows)

def print_rectangle_dollar(rows, cols):
    print("\nRectangle Dollar Pattern:")
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                print('$', end=' ')
            else:
                print(' ', end=' ')
        print()

# Get input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Print square star pattern
print_square_star(rows)

# Print rectangle dollar pattern
print_rectangle_dollar(rows, cols)
