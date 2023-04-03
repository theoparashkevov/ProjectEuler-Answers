# Read in the names from the file and sort them
with open('p022_names.txt') as f:
    names = f.read().replace('"', '').split(',')
names.sort()

# Define a function to compute the name score
def name_score(name):
    return sum(ord(c)-64 for c in name)

# Compute the total name score for all names
total_name_score = sum((i+1) * name_score(names[i]) for i in range(len(names)))

print(total_name_score)
