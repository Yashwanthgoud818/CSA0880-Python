def generate_pythagorean_triples(limit):
    triples = []
    for a in range(1, limit):
        for b in range(a, limit):
            c_square = a**2 + b**2
            c = int(c_square**0.5)
            if c <= limit and c_square == c**2:
                triples.append((a, b, c))
    return triples

# Example usage:
limit = int(input("Enter the limit: "))
pythagorean_triples = generate_pythagorean_triples(limit)
print(f"Pythagorean triples with values smaller than {limit}:")
for triple in pythagorean_triples:
    print(triple)
