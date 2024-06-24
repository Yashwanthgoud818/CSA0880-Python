def print_pattern(num, max_prints):
    num_str = str(num)
    length = len(num_str)
    
    for i in range(1, max_prints + 1):
        for j in range(i):
            print(num_str, end=" ")
        print()

# Sample Input
num = int(input("Enter the number to be printed: "))
max_prints = int(input("Max Number of time printed: "))

# Print the pattern
print_pattern(num, max_prints)
