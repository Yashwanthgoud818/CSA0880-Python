import math

def find_square_root(number):
    # Calculate the square root using math.sqrt
    square_root = math.sqrt(number)
    
    # Check if the square root is an integer (perfect square)
    if square_root.is_integer():
        positive_root = int(square_root)
        negative_root = -positive_root
        return f"Square Root: {positive_root}, {negative_root}"
    else:
        return "The number is not a perfect square."

# Example usage:
number = int(input("Enter the number: "))

result = find_square_root(number)
print(result)
