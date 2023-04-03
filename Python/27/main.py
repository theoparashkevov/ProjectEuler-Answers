def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Initialize variables to store the maximum number of consecutive primes and the corresponding coefficients
max_consecutive_primes = 0
max_a = 0
max_b = 0

# Iterate over possible values of a and b
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while is_prime(n**2 + a*n + b):
            n += 1
        if n > max_consecutive_primes:
            max_consecutive_primes = n
            max_a = a
            max_b = b

print(max_a * max_b)
