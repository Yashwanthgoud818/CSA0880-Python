def calculate_simple_interest(principal, years, senior_citizen):
    if senior_citizen.lower() == 'y':
        rate_of_interest = 12  # 12% interest rate for senior citizens
    else:
        rate_of_interest = 10  # 10% interest rate for others
    
    interest = (principal * rate_of_interest * years) / 100
    return interest

# Get input from user
principal = float(input("Enter the principal amount: "))
years = int(input("Enter the number of years: "))
senior_citizen = input("Is customer senior citizen (y/n): ")

# Calculate simple interest
interest = calculate_simple_interest(principal, years, senior_citizen)

# Print the calculated interest
print(f"Interest: {interest}")
