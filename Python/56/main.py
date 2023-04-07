def digital_sum(n):
    return sum(int(digit) for digit in str(n))

max_sum = 0

for a in range(1, 100):
    for b in range(1, 100):
        num = a ** b
        digit_sum = digital_sum(num)
        if digit_sum > max_sum:
            max_sum = digit_sum

print(max_sum)
