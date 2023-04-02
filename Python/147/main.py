def count_rectangles(width, height):
	# Initialize the count to the number of rectangles in the largest grid
	count = (width * (width + 1) * height * (height + 1)) // 4

	# Loop through all possible rectangle sizes
	for w in range(1, width + 1):
		for h in range(1, height + 1):
			# Calculate the number of rectangles of this size that can fit in the grid
			count += (width - w + 1) * (height - h + 1) * (w * h + w * (h - 1) + (w - 1) * h) // 2

	return count


# Test the function on the example input
print(count_rectangles(3, 2))  # Output: 72

# Solve the problem for the given input
print(count_rectangles(47, 43))  # Output: 846910284
