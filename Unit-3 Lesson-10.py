import math

def generate_pythagorean_triples(limit):
    triples = []

    for n in range(3, limit + 1):
        if n % 2 == 1:  # n is odd
            a = n
            b = (n**2 - 1) // 2
            c = (n**2 + 1) // 2
        else:  # n is even
            a = n
            m = n // 2
            b = m**2 - 1
            c = m**2 + 1

        triples.append([a, b, c])

    return triples

# Test the function with a limit, e.g., 12
upper_limit = 12
triples = generate_pythagorean_triples(upper_limit)
for triple in triples:
    a, b, c = triple
    print(f"[{a}, {b}, {c}] => {a}^2 + {b}^2 = {c}^2 = {a**2 + b**2}")
