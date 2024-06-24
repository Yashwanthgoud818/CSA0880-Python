def check_eligibility(age):
    if age >= 18:
        print("You are eligible to vote!")
    else:
        years_left = 18 - age
        print(f"You are not eligible to vote yet. You need to wait {years_left} more years.")

# Example usage:
age = int(input("Enter your age: "))
check_eligibility(age)
