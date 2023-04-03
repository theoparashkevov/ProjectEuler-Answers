def fibonacci(n):
    # Initialize the first two Fibonacci numbers
    fib_0 = 0
    fib_1 = 1

    # Compute Fibonacci numbers until we reach the desired index
    for i in range(n):
        # Update the Fibonacci numbers
        fib_0, fib_1 = fib_1, fib_0 + fib_1

    return fib_0

# Iterate over Fibonacci numbers until we find one with 1000 digits
n = 0
while True:
    fib_n = fibonacci(n)
    if len(str(fib_n)) == 1000:
        break
    n += 1

# Print the index of the first Fibonacci number with 1000 digits
print(n)
