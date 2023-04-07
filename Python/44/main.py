import math

def is_pentagonal(n):
    # Check if n is a pentagonal number
    x = (1 + math.sqrt(1 + 24 * n)) / 6
    return x == int(x)

def generate_pentagonal_numbers(n):
    # Generate the first n pentagonal numbers
    pentagonal_numbers = set()
    for i in range(1, n+1):
        pentagonal_numbers.add(i * (3*i - 1) // 2)
    return pentagonal_numbers

def solve():
    pentagonal_numbers = generate_pentagonal_numbers(10000)
    min_difference = float('inf')

    for j in range(1, 5000):
        for k in range(j+1, 5000):
            p_j, p_k = j * (3*j - 1) // 2, k * (3*k - 1) // 2
            if p_k - p_j >= min_difference:
                # No need to continue if difference is already greater than min_difference
                break
            if p_k + p_j in pentagonal_numbers and p_k - p_j in pentagonal_numbers:
                if p_k - p_j < min_difference:
                    min_difference = p_k - p_j

    return min_difference

print(solve())
