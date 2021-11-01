from sympy import primerange
list_of_prime_gaps = [x - y for x, y in zip(primerange(3, 40000),
primerange(1, 40000))]
def a(n):
    saved = set()
    for i in range(1, len(list_of_prime_gaps)-n):
        sequence = list_of_prime_gaps[i:i+n]
        if tuple(sequence) in saved:
            return i + n - 1
        saved.add(tuple(sequence))
    return None
for n in range(1, 14):
    print(a(n), end=", ")
