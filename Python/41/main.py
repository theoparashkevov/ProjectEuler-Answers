# importing the permutations method
from itertools import permutations

def is_prime(n):
    """Function to check if
    the given number is prime"""
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# permutations of numbers from 1-7
p = permutations('1234567')

# for loop to loop from reverse order
# from higher to lower
for i in list(p)[::-1]:
    if int(i[6]) % 2 != 0:
        number = int(''.join(i))
        if (number+1) % 6 == 0 or (number-1) % 6 == 0:
            if is_prime(number):
                print(number)
                break

