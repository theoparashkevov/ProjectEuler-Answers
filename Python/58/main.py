def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

side_length = 3
diagonal_num = 1
num_primes = 0
total_diagonal = 1

while True:
    # top right diagonal
    diagonal_num += side_length - 1
    if is_prime(diagonal_num):
        num_primes += 1
    # top left diagonal
    diagonal_num += side_length - 1
    if is_prime(diagonal_num):
        num_primes += 1
    # bottom left diagonal
    diagonal_num += side_length - 1
    if is_prime(diagonal_num):
        num_primes += 1
    # bottom right diagonal
    diagonal_num += side_length - 1
    if is_prime(diagonal_num):
        num_primes += 1
    
    # update total diagonal count
    total_diagonal += 4
    
    # check if ratio falls below 10%
    if num_primes / total_diagonal < 0.1:
        break
    
    # increment side length by 2
    side_length += 2

print(side_length)
