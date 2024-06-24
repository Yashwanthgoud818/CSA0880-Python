def sum_of_digits(num):
    # Calculate sum of digits
    sum_digits = sum(int(digit) for digit in str(num))
    
    # If sum is greater than 9, continue to sum digits until single digit is obtained
    while sum_digits > 9:
        sum_digits = sum(int(digit) for digit in str(sum_digits))
    
    return sum_digits

# Example usage:
N = int(input("Enter N value: "))
number = int(input(f"Enter {N} digit number: "))

# Calculate and print sum of digits
sum_digits_result = sum_of_digits(number)
print(f"Sum of {N} digit number: {sum_digits_result}")
