def contains_same_digits(number_1, number_2):
    n1 = str(number_1)
    n2 = str(number_2)

    if len(n1) != len(n2):
        return False

    for digit_character in n1:
        if digit_character not in n2:
            return False

    for digit_character in n2:
        if digit_character not in n1:
            return False

    return True


def check_multiples(number):
    number_2x = 2 * number
    number_3x = 3 * number
    number_4x = 4 * number
    number_5x = 5 * number
    number_6x = 6 * number

    if not contains_same_digits(number, number_2x):
        return False

    if not contains_same_digits(number, number_3x):
        return False

    if not contains_same_digits(number, number_4x):
        return False

    if not contains_same_digits(number, number_5x):
        return False

    if not contains_same_digits(number, number_6x):
        return False

    return True


if __name__ == '__main__':

    current_number = 1
    multiples_are_valid = False

    while multiples_are_valid is False:
        current_number += 1
        multiples_are_valid = check_multiples(current_number)

        if current_number % 20 == 0:
            print(f'{current_number} [{multiples_are_valid}]', end='\n')
        else:
            print(f'{current_number} [{multiples_are_valid}]', end='  ')

    print('\n\n')
    print(
        f'{current_number} [{multiples_are_valid}] [2x] {2 * current_number} [3x] {3 * current_number} [4x] {4 * current_number} [5x] {5 * current_number} [6x] {6 * current_number}',
        end='\n')
