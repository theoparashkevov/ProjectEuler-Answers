

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_digit_factorial(n):
    total = 0
    for digit in str(n):
        total += factorial(int(digit))
    return total == n


result = 0
for n in range(3, 1000000):
    if is_digit_factorial(n):
        result += n

print(result)
