from math import sqrt

def is_prime(n):
    """Return True if n is prime, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_permutation(n1, n2):
    """Return True if n1 and n2 are permutations of each other, False otherwise."""
    return sorted(str(n1)) == sorted(str(n2))

primes = [n for n in range(1000, 10000) if is_prime(n)]

for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        p1, p2 = primes[i], primes[j]
        p3 = 2 * p2 - p1
        if p3 in primes and is_permutation(p1, p2) and is_permutation(p1, p3):
            print(str(p1) + str(p2) + str(p3))
