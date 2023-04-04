def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def rotations(n):
    """
    Generates all the possible rotations of a number.
    """
    rotations = []
    s = str(n)
    for i in range(len(s)):
        rotations.append(int(s[i:] + s[:i]))
    return rotations

count = 0
for i in range(2, 1000000):
    if all(is_prime(x) for x in rotations(i)):
        count += 1

print(count)
