def sum_of_divisors(n):
    """Return the sum of proper divisors of n."""
    divisors = [1]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

# Iterate over all pairs of numbers under 10000
amicable_sum = 0
for i in range(1, 10000):
    for j in range(i+1, 10000):
        # Check if i and j are amicable
        if sum_of_divisors(i) == j and sum_of_divisors(j) == i:
            amicable_sum += i + j

print(amicable_sum)
