def print_hollow_square(symbol, size):
    print(f"Hollow Square Symbol Pattern with '{symbol}':")
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print(symbol, end=' ')
            else:
                print(' ', end=' ')
        print()

# Get input from user
symbol = input("Enter the symbol you want to use: ")
size = int(input("Enter the size of the square: "))

# Print hollow square symbol pattern
print_hollow_square(symbol, size)
