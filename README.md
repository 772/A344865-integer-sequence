# A344865 integer sequence

a(n) is the largest k such that no subsequence of n numbers appears more than once in the sequence of the first k prime gaps while overlapping subsequences are allowed.

```2, 5, 6, 7, 19, 59, 88, 89, 1213, 1214, 3876, 3877, 3878```

http://oeis.org/A344865

When using a huge amount of primes, this software proves that n = 14 is the first n > 1 where a(n) > a(n-1)^2. And this is interesting, because it means that recursive formulas with 14 input parameters are able to generate a lot of prime numbers. You would do this by creating a recursive formula f(p) that generates the next prime gap p by using p-1, p-2, p-3, ... p-14.
