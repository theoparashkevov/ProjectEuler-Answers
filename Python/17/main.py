# Define a dictionary mapping numbers to their word representations
word_dict = {
	0: '',
	1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
	6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
	11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
	16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
	30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
	80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'
}


def num_letters(n):
	if n <= 20:
		return len(word_dict[n])
	elif n < 100:
		return len(word_dict[n // 10 * 10]) + num_letters(n % 10)
	elif n < 1000:
		hundred_letters = len(word_dict[n // 100]) + len(word_dict[100])
		if n % 100 == 0:
			return hundred_letters
		else:
			return hundred_letters + len('and') + num_letters(n % 100)
	else:
		return len(word_dict[n // 1000]) + len(word_dict[1000])


total_letters = sum(num_letters(n) for n in range(1, 1001))
print(total_letters)
