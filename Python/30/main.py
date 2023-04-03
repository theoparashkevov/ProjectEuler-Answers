# Define a function to check if a number can be written as the sum of the fifth powers of its digits
def is_sum_of_fifth_powers(n):
    return n == sum(int(digit) ** 5 for digit in str(n))

# Initialize variables to store the sum and the upper bound for the search
sum_of_numbers = 0
upper_bound = 9 ** 5 * 6 # the maximum number that can be written as the sum of the fifth powers of its digits

# Iterate over all the numbers that can be written as the sum of the fifth powers of their digits
for number in range(2, upper_bound + 1):
    if is_sum_of_fifth_powers(number):
        sum_of_numbers += number

# Print the sum of the numbers that can be written as the sum of the fifth powers of their digits
print(sum_of_numbers)
