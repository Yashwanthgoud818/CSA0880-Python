def print_full_rectangle(symbol, width, height):
    for _ in range(height):
        print(symbol * width)

def print_hollow_rectangle(symbol, width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            print(symbol * width)
        else:
            print(symbol + ' ' * (width - 2) + symbol)

# Get user inputs
symbol = input("Enter the symbol to use: ")
width = int(input("Enter the width of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))
pattern_type = input("Enter 'F' for full rectangle or 'H' for hollow rectangle: ")

# Print the chosen rectangle pattern
if pattern_type.upper() == 'F':
    print_full_rectangle(symbol, width, height)
elif pattern_type.upper() == 'H':
    print_hollow_rectangle(symbol, width, height)
else:
    print("Invalid choice. Please enter 'F' or 'H'.")
