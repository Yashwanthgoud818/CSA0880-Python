def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is the only even prime number
    if num % 2 == 0:
        return False  # other even numbers are not prime
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def count_prime_composite(numbers):
    prime_count = 0
    composite_count = 0

    for num in numbers:
        if is_prime(num):
            prime_count += 1
        else:
            composite_count += 1

    return prime_count, composite_count

# Example usage:
numbers = [4, 54, 29, 71, 7, 59, 98, 23]

prime_count, composite_count = count_prime_composite(numbers)

print(f"Composite number: {composite_count}")
print(f"Prime number: {prime_count}")
