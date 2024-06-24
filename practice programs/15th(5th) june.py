def number_of_factors(num):
    if num == 0:
        return 0  # 0 has infinite factors, but let's consider 0 has 0 factors for simplicity
    count = 0
    for i in range(1, abs(num) + 1):
        if num % i == 0:
            count += 1
    return count

def nth_factor(num, n):
    if num == 0:
        return None  # Cannot find factors for 0
    factors = []
    for i in range(1, abs(num) + 1):
        if num % i == 0:
            factors.append(i)
    if n <= len(factors):
        return factors[n - 1]
    else:
        return None  # Nth factor does not exist

# Test cases
test_cases = [
    (512, 6),
    (343, 7),
    (1024, 0),
    (-6561, 3),
    (0, 2)
]

for num, n in test_cases:
    num_factors = number_of_factors(num)
    nth = nth_factor(num, n)
    print(f"Given Number: {num}")
    print(f"Number of factors = {num_factors}")
    if nth is not None:
        print(f"{n}th factor of {num} = {nth}")
    else:
        print(f"{n}th factor of {num} does not exist")
    print()
