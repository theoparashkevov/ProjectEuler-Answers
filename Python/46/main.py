def is_prime(n):
    """Return True if n is prime, else False."""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_smallest_odd_composite():
    primes = [2, 3, 5, 7]
    n = 9
    while True:
        if is_prime(n):
            primes.append(n)
        else:
            found = False
            for p in primes:
                remainder = (n - p) / 2
                if remainder == int(remainder) and (int(remainder) ** 0.5).is_integer():
                    found = True
                    break
            if not found:
                return n
        n += 2

print(find_smallest_odd_composite())
