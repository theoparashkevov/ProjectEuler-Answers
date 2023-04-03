def recurring_cycle(n):
    """Compute the length of the recurring cycle of 1/n."""
    remainders = {}
    remainder = 1
    i = 0
    while remainder != 0 and remainder not in remainders:
        remainders[remainder] = i
        remainder = remainder * 10 % n
        i += 1
    return i - remainders.get(remainder, 0)

longest_cycle = 0
d = 0

# Iterate over values of d from 2 to 999
for i in range(2, 1000):
    cycle_length = recurring_cycle(i)
    if cycle_length > longest_cycle:
        longest_cycle = cycle_length
        d = i

print(d)
