def decimal_to_binary(decimal_num):
    return bin(decimal_num).replace("0b", "")

def decimal_to_octal(decimal_num):
    return oct(decimal_num).replace("0o", "")

# Example usage:
decimal_number = int(input("Decimal Number: "))

binary_number = decimal_to_binary(decimal_number)
octal_number = decimal_to_octal(decimal_number)

print(f"Binary Number = {binary_number}")
print(f"Octal = {octal_number}")
