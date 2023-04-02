import math

# Calculate the factorial of 100
fact = math.factorial(100)

# Convert the factorial to a string
fact_str = str(fact)

# Sum up the digits of the factorial
digit_sum = 0
for digit in fact_str:
    digit_sum += int(digit)

print(digit_sum)
