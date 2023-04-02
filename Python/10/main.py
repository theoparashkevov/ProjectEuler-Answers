def sum_of_primes(n):
	# Initialize a list of booleans indicating whether each number is prime
	is_prime = [True] * n

	# 0 and 1 are not prime
	is_prime[0] = is_prime[1] = False

	# Use the Sieve of Eratosthenes to mark all multiples of primes as not prime
	for i in range(2, int(n ** 0.5) + 1):
		if is_prime[i]:
			for j in range(i ** 2, n, i):
				is_prime[j] = False

	# Sum up all the primes
	return sum(i for i in range(n) if is_prime[i])


'''
The sum_of_primes function takes an integer argument n and returns the sum of all primes less than n.
It first initializes a list of booleans called is_prime, where each index represents a number from 0 to n-1,
and each value indicates whether that number is prime or not. The first two indices (0 and 1) are set to False,
since they are not prime.

Then, the function uses the Sieve of Eratosthenes algorithm to mark all multiples of primes as not prime.
The algorithm works as follows: starting with the first prime (2), mark all its multiples as not prime.
Then move to the next prime that hasn't been marked, and repeat. When you've gone through all the primes
up to the square root of n, all remaining unmarked numbers are prime.

Finally, the function sums up all the primes using a generator expression,
which generates the prime numbers from 0 to n-1 and filters out the non-primes based on the is_prime list.
Testing the function on the example input should give the expected output of 17, and running it on the given input
should give the answer of 142913828922.
'''

# Test the function on the example input
print(sum_of_primes(10))  # Output: 17

# Solve the problem for the given input
print(sum_of_primes(2000000))  # Output: 142913828922
