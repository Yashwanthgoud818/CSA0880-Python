def sort_names(names, order):
    if order.lower() == 'a':
        return sorted(names)
    elif order.lower() == 'd':
        return sorted(names, reverse=True)
    else:
        return "Invalid order choice. Please enter 'A' for ascending or 'D' for descending."

# Input names
names = []
print("Enter names (type 'done' to finish):")
while True:
    name = input()
    if name.lower() == 'done':
        break
    names.append(name)

# Get sorting order
order = input("Order (A/D): ")

# Sort and display the names
sorted_names = sort_names(names, order)
if isinstance(sorted_names, list):
    print("Sorted names:")
    for name in sorted_names:
        print(name)
else:
    print(sorted_names)
