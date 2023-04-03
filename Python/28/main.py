# Initialize variables to store the sum of the diagonals and the current number in the spiral
diagonal_sum = 1
current_number = 1

# Iterate over the layers of the spiral
for layer in range(1, 501):
	# Compute the four corners of the current layer and add them to the diagonal sum
	for i in range(4):
		current_number += 2 * layer
		diagonal_sum += current_number

print(diagonal_sum)
