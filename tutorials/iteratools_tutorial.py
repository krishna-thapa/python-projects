# itertools: product, permutations, combinations, accumulate, groupby, and inifinte iterators

from itertools import product, permutations, combinations, accumulate

a = [1, 2, 3]
b = [4]
prod = product(a, b, repeat=1)
print(list(prod))

perm = permutations(a, 2)
print(list(perm))

comb = combinations(a, 2)
print(list(comb))
