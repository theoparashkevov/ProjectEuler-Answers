from math import factorial

count = 0
for n in range(1, 101):
    for r in range(1, n+1):
        nCr = factorial(n) // (factorial(r) * factorial(n-r))
        if nCr > 1000000:
            count += 1

print(count)
