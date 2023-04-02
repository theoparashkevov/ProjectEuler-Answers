import itertools
from copy import deepcopy

A_LIST = []
B_LIST = []

ALL_COMBINATIONS = []


def compress(arg_list: list):
    tmp_list = arg_list
    number_of_combinations_to_add = 0

    while len(tmp_list) > 2:
        # ALL_COMBINATIONS.append(deepcopy(tmp_list))
        tmp_list.sort(reverse=True)
        ALL_COMBINATIONS.append(str(tmp_list))
        var_1 = tmp_list.pop()
        var_2 = tmp_list.pop()
        tmp_list.append(var_1 + var_2)
        number_of_combinations_to_add += 1

    if len(tmp_list) == 2:
        # ALL_COMBINATIONS.append(deepcopy(tmp_list))
        tmp_list.sort(reverse=True)
        ALL_COMBINATIONS.append(str(tmp_list))
        number_of_combinations_to_add += 1

    return number_of_combinations_to_add


def split_into_lists(number: int):
    number_of_combinations_to_return = 0
    global A_LIST
    global B_LIST

    # Reallocate
    if len(A_LIST) == 0:
        A_LIST.append(number)
    else:
        var_number = A_LIST.pop()
        A_LIST.append(var_number - 1)
        B_LIST.append(1)

    #print(A_LIST)
    #print(B_LIST)
    #print('---')

    RESULT_LIST = A_LIST + B_LIST
    RESULT_LIST.sort(reverse=True)

    if RESULT_LIST.count(1) == len(RESULT_LIST):
        # ALL_COMBINATIONS.append(deepcopy(RESULT_LIST))
        ALL_COMBINATIONS.append(str(RESULT_LIST))
        number_of_combinations_from_compress = 1
    else:
        number_of_combinations_from_compress = compress(RESULT_LIST)




    # Recursion
    number_of_combinations_from_split = 0
    if number > 1:
        number_of_combinations_from_split = split_into_lists(number - 1)

    number_of_combinations_to_return += number_of_combinations_from_compress
    number_of_combinations_to_return += number_of_combinations_from_split

    return number_of_combinations_to_return


if __name__ == '__main__':
    '''
    number_to_find = 6

    split_into_lists(number_to_find)

    ALL_COMBINATIONS.sort(reverse=True)

    ALL_COMBINATIONS = list(dict.fromkeys(ALL_COMBINATIONS))
    total_combinations = len(ALL_COMBINATIONS)

    print('\n\nRESULTS')
    print(f'Number of combinations for [{number_to_find}] = {total_combinations}')
    print(ALL_COMBINATIONS)
    '''
    target = 6
    ns = range(1, target)  # 1 to (n-1)
    ways = [1] + [0] * target

    print('ways = ', ways)

    for n in ns: # i belongs to [1, n-1]
        print(ways)
        for i in range(n, target + 1): # j belongs to [i, n]
            ways[i] += ways[i - n]

    print(ways)
    print("Number of ways", target, "can be written as a \nsum of at least two positive integers:", ways[target])
