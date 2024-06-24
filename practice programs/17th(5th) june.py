def calculate_bonus(grade, salary):
    if salary < 0:
        return None, None, None
    
    base_salary = salary
    bonus_percentage = 0
    
    if grade.upper() == 'A':
        bonus_percentage = 5
    elif grade.upper() == 'B':
        bonus_percentage = 10
    else:
        return None, None, None  # Invalid grade
    
    if salary < 10000:
        bonus_percentage += 2
    
    bonus_amount = (bonus_percentage / 100) * salary
    total_salary = base_salary + bonus_amount
    
    return base_salary, bonus_amount, total_salary

# Test cases
test_cases = [
    ('A', 8000),
    ('C', 60000),
    ('B', 0),
    ('A', 38000),
    ('B', -8000)
]

for grade, salary in test_cases:
    base_salary, bonus_amount, total_salary = calculate_bonus(grade, salary)
    if base_salary is None:
        print(f"Invalid input: Grade '{grade}' or Salary '{salary}'")
    else:
        print(f"Grade of employee: {grade}")
        print(f"Employee salary: {base_salary}")
        print(f"Bonus: {bonus_amount}")
        print(f"Total to be paid: {total_salary}")
        print()
