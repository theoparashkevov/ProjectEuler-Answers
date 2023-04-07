def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]

def max_sum_consecutive_primes(n):
    primes = sieve_of_eratosthenes(n)
    prime_set = set(primes)
    max_sum = 0
    max_length = 0
    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            consecutive_sum = sum(primes[i:j+1])
            if consecutive_sum > n:
                break
            if consecutive_sum in prime_set:
                max_sum = consecutive_sum
                max_length = j - i + 1
    return max_sum

print(max_sum_consecutive_primes(1000000))
