def calculate_tax(income):
    if income <= 150000:
        tax = 0
    elif 150001 <= income <= 300000:
        tax = 150000 * 0.05 + (income - 150000) * 0.10
    elif 300001 <= income <= 500000:
        tax = 150000 * 0.05 + 150000 * 0.10 + (income - 300000) * 0.20
    else:
        tax = 150000 * 0.05 + 150000 * 0.10 + 200000 * 0.20 + (income - 500000) * 0.30
    return tax

# Sample Input
income = float(input("Enter the income: "))

# Calculate and display tax
tax = calculate_tax(income)
print(f"Tax = {tax}")
