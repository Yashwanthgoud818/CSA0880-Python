def sort_letters(word):
    # Convert the word into a list of characters
    letters = list(word)
    
    # Sort the letters alphabetically in normal order
    normal_order = sorted(letters)
    
    # Sort the letters alphabetically in reverse order
    reverse_order = sorted(letters, reverse=True)
    
    # Convert lists back to strings
    normal_order_str = ' '.join(normal_order)
    reverse_order_str = ' '.join(reverse_order)
    
    return normal_order_str, reverse_order_str

# Example usage:
word = input("Enter the word: ")

normal_order, reverse_order = sort_letters(word)

print(f"Alphabetical Order Normal: {normal_order}")
print(f"Alphabetical Order Reverse: {reverse_order}")
