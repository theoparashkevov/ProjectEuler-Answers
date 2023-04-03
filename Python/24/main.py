from itertools import permutations

lexi_perm = list(permutations('0123456789'))

solution = ''.join(lexi_perm[999999])

print(solution)
