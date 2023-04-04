def is_palindrome(n):
    """Returns True if n is a palindrome, False otherwise."""
    return str(n) == str(n)[::-1]

def is_palindrome_base_2(n):
    """Returns True if n is palindromic in base 2, False otherwise."""
    binary = bin(n)[2:]  # Convert n to binary, without the '0b' prefix
    return is_palindrome(binary)

def sum_palindromic_numbers():
    """Finds the sum of all numbers less than 1 million that are palindromic in both base 10 and base 2."""
    palindromic_numbers = []
    for i in range(1, 1000000):
        if is_palindrome(i) and is_palindrome_base_2(i):
            palindromic_numbers.append(i)
    return sum(palindromic_numbers)

print(sum_palindromic_numbers())  # Output: 872187
