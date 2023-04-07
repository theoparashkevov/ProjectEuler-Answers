import string

# Function to calculate the alphabetical position of a letter
def alphabet_position(letter):
    return string.ascii_uppercase.index(letter) + 1

# Function to check if a number is a triangular number
def is_triangular(n):
    return ((-1 + (1 + 8 * n) ** 0.5) / 2).is_integer()

# Read the file containing the list of words
with open('p042_words.txt', 'r') as file:
    words = file.read().replace('"', '').split(',')

# Calculate the sum of the alphabetical positions of each letter in each word
word_sums = [sum(alphabet_position(letter) for letter in word) for word in words]

# Count the number of triangle words
triangle_word_count = sum(is_triangular(sum) for sum in word_sums)

print(triangle_word_count)
