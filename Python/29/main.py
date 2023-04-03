# Initialize a set to store the distinct terms
distinct_terms = set()

# Iterate over all pairs of integers (a, b) in the specified range
for a in range(2, 101):
    for b in range(2, 101):
        # Compute the value of a^b and add it to the set
        distinct_terms.add(a ** b)

# Print the number of distinct terms in the set
print(len(distinct_terms))
