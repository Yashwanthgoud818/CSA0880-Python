def is_palindrome(word):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]

def is_number_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]

def check_palindrome(case, input_value):
    if case == 1:
        if is_palindrome(input_value):
            return "Palindrome"
        else:
            return "Not Palindrome"
    elif case == 2:
        if is_number_palindrome(input_value):
            return "Palindrome"
        else:
            return "Not Palindrome"
    else:
        return "Invalid Case"

# Example usage:
case = int(input("Case (1 for word, 2 for number): "))
input_value = input("Enter the input value: ")

result = check_palindrome(case, input_value)
print(result)
