def check_number_and_print(number):
    if number % 2 == 0:
        next_even = number + 2
        print(f"Result Number: {next_even}")
    else:
        previous_odd = number - 2
        print(f"Result Number: {previous_odd}")

# Taking input from user
num = int(input("Enter the number: "))

# Calling the function to check and print the result
check_number_and_print(num)
