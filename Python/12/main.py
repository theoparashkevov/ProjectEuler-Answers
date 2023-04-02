def get_triangle_number(n):
	return n * (n + 1) // 2


def get_num_divisors(n):
	count = 0
	for i in range(1, int(n ** 0.5) + 1):
		if n % i == 0:
			count += 2
	if int(n ** 0.5) ** 2 == n:
		count -= 1
	return count


'''
The get_triangle_number(n) function returns the nth triangle number using the formula n * (n + 1) // 2.

The get_num_divisors(n) function calculates the number of divisors of a given number n using a brute force approach.
It iterates from 1 to the square root of n and counts the number of divisors.
If n is a perfect square, it subtracts 1 from the count to avoid double-counting the square root.

The main loop iterates over the triangle numbers until it finds the first triangle number with over 500 divisors.
Once it finds the solution, it prints it and breaks out of the loop.
'''

n = 1
while True:
	triangle_num = get_triangle_number(n)
	num_divisors = get_num_divisors(triangle_num)
	if num_divisors > 500:
		print(triangle_num)
		break
	n += 1
