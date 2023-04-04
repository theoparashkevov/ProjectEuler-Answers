def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i ** 2, n + 1, i):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]


def is_truncatable_prime(n, primes):
    # Check if n is a truncatable prime from left to right
    n_str = str(n)
    for i in range(1, len(n_str)):
        if int(n_str[i:]) not in primes:
            return False

    # Check if n is a truncatable prime from right to left
    while n > 0:
        if n not in primes:
            return False
        n //= 10
    return True


def sum_of_truncatable_primes():
    primes = set(sieve_of_eratosthenes(1_000_000))
    truncatable_primes = []
    for p in primes:
        if is_truncatable_prime(p, primes) and p > 7:
            truncatable_primes.append(p)
            if len(truncatable_primes) == 11:
                break
    return sum(truncatable_primes)


print(sum_of_truncatable_primes())  # output: 748317
