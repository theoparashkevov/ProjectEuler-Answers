# Define a function to compute the sum of proper divisors of a number
def sum_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

# Find all abundant numbers up to 28123
abundant_numbers = set()
for i in range(1, 28124):
    if sum_divisors(i) > i:
        abundant_numbers.add(i)

# Find all numbers that can be written as the sum of two abundant numbers
sums_of_abundant_numbers = set()
for x in abundant_numbers:
    for y in abundant_numbers:
        if x + y > 28123:
            break
        sums_of_abundant_numbers.add(x + y)

# Compute the sum of all positive integers that cannot be written as the sum of two abundant numbers
non_abundant_sums = sum(i for i in range(1, 28124) if i not in sums_of_abundant_numbers)

print(non_abundant_sums)
