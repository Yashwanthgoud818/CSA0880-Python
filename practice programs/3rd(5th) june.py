def calculate_grade(marks):
    total = sum(marks)
    aggregate = total / len(marks)
    
    if aggregate >= 75:
        grade = "DISTINCTION"
    elif 60 <= aggregate < 75:
        grade = "FIRST DIVISION"
    elif 50 <= aggregate < 60:
        grade = "SECOND DIVISION"
    elif 40 <= aggregate < 50:
        grade = "THIRD DIVISION"
    else:
        grade = "FAIL"
    
    return total, aggregate, grade

# Input marks
marks = []
subjects = ["python", "c programming", "Mathematics", "Physics"]

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter the marks in {subject}: "))
            if mark < 0 or mark > 100:
                raise ValueError("Marks should be between 0 and 100.")
            marks.append(mark)
            break
        except ValueError as e:
            print(e)

# Calculate total, aggregate, and grade
total, aggregate, grade = calculate_grade(marks)

# Display results
print(f"Total = {total}")
print(f"Aggregate = {aggregate}")
print(grade)
