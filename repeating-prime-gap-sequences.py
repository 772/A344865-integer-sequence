from sympy import primerange
list_of_prime_gaps = [x - y for x, y in zip(primerange(3, 40000), primerange(1, 40000))]
def a(n):
    saved = set()
    for i in range(1, len(list_of_prime_gaps)-n):
        sequence = list_of_prime_gaps[i:i+n]
        if tuple(sequence) in saved:
            return sequence, i
        saved.add(tuple(sequence))
    return None, None
for n in range(1, 15): # Trivia: n = 14 is the first n > 1 where a(n) > a(n-1)^2.
    sequence, position = a(n)
    print("n =", n, end=": ")
    if sequence:
        print("At position", str(position + 1), "the sequence", str(sequence)[1:-1], "occurs a second time.")
    else:
        print("No repetition found while searching through the first", len(list_of_prime_gaps), "prime gaps.")
