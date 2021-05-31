from sympy import primerange
list_of_prime_gaps = [x - y for x, y in zip(primerange(3, 40000), primerange(1, 40000))]
def a(n):
    saved = set()
    for i in range(1, len(list_of_prime_gaps)-n):
        sequence = list_of_prime_gaps[i:i+n]
        if tuple(sequence) in saved:
            return i + n - 1
        saved.add(tuple(sequence))
    return None
for n in range(1, 15): # Trivia: n = 14 is the first n > 1 where a(n) > a(n-1)^2.
    num_no_repetition = a(n)
    if num_no_repetition:
        print(str(num_no_repetition), "is the amount of first prime gaps without a repetive sequence of", n, "numbers.")
    else:
        print("No repetition of length", n, "found while searching through the first", len(list_of_prime_gaps), "prime gaps.")
