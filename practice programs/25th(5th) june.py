def is_harshad_number(number):
    # Convert number to string to iterate over digits
    number_str = str(number)
    
    # Calculate sum of digits
    sum_of_digits = sum(int(digit) for digit in number_str)
    
    # Check if number is divisible by sum of its digits
    return number % sum_of_digits == 0

# Example usage:
number = int(input("Enter the number: "))

if is_harshad_number(number):
    print("Given number is Harshad number")
else:
    print("Given number is not Harshad number")
