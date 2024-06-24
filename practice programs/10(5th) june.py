def sum_of_proper_divisors(num):
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors

def is_perfect_number(num):
    return num == sum_of_proper_divisors(num)

def first_n_perfect_numbers(n):
    perfect_numbers = []
    num = 1
    while len(perfect_numbers) < n:
        if is_perfect_number(num):
            perfect_numbers.append(num)
        num += 1
    return perfect_numbers

# Example usage:
N = 3
perfect_numbers = first_n_perfect_numbers(N)
print(f"First {N} perfect numbers are:", ", ".join(map(str, perfect_numbers)))
