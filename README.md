# repeating-prime-gap-sequences

a(n) is the position of the second occurence of a length n sequence in the list of prime gaps.

When using a huge amount of primes, this software proves that n = 14 is the first n > 1 where a(n) > a(n-1)^2.

```
n = 1: At position 3 the sequence 2 occurs a second time.
n = 2: At position 5 the sequence 2, 4 occurs a second time.
n = 3: At position 5 the sequence 2, 4, 2 occurs a second time.
n = 4: At position 5 the sequence 2, 4, 2, 4 occurs a second time.
n = 5: At position 16 the sequence 6, 2, 6, 4, 2 occurs a second time.
n = 6: At position 55 the sequence 6, 6, 2, 6, 4, 2 occurs a second time.
n = 7: At position 83 the sequence 2, 6, 4, 6, 8, 4, 2 occurs a second time.
n = 8: At position 83 the sequence 2, 6, 4, 6, 8, 4, 2, 4 occurs a second time.
n = 9: At position 1206 the sequence 6, 4, 12, 8, 6, 12, 4, 6, 12 occurs a second time.
n = 10: At position 1206 the sequence 6, 4, 12, 8, 6, 12, 4, 6, 12, 6 occurs a second time.
n = 11: At position 3867 the sequence 6, 14, 4, 26, 4, 2, 12, 10, 8, 4, 8 occurs a second time.
n = 12: At position 3867 the sequence 6, 14, 4, 26, 4, 2, 12, 10, 8, 4, 8, 12 occurs a second time.
n = 13: At position 3867 the sequence 6, 14, 4, 26, 4, 2, 12, 10, 8, 4, 8, 12, 4 occurs a second time.
n = 14: No repetition found while searching through the first 14953689 prime gaps.
```
