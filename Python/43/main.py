from itertools import permutations

def has_property(num):
    # Check if the number has the sub-string divisibility property
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        sub_num = int(num[i:i+3])
        if sub_num % primes[i-1] != 0:
            return False
    return True

# Generate all pandigital numbers
digits = "0123456789"
pandigitals = list(permutations(digits))

# Convert tuples to integers
pandigitals = [int("".join(p)) for p in pandigitals]

# Check each pandigital number for the sub-string divisibility property
total = 0
for num in pandigitals:
    if has_property(str(num)):
        total += num

print(total)
