# itertools: product, permutations, combinations, accumulate, groupby, and inifinte iterators

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
import operator
from operator import itemgetter

a = [1, 2, 3]
b = [4]
prod = product(a, b, repeat=1)
print(list(prod))

perm = permutations(a, 2)
print(list(perm))

comb = combinations(a, 2)
print(list(comb))

comb_repl = combinations_with_replacement(a, 2)
print(list(comb_repl))

accum = accumulate(a)
print(list(accum))

accum_multi = accumulate(a, func=operator.mul)
print(list(accum_multi))

b = [1, 2, 3, 8, 3, 4]
accum_max = accumulate(b, func=max)
print(list(accum_max))


def smaller_than_3(x):
    return x < 3


group_obj = groupby(b, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

print("Use of lambda")

# NOTE that for groupby to work properly, mylist has to be sorted by the grouping key

group_obj2 = groupby(b, key=lambda x: x > 5)
for key, value in group_obj2:
    print(key, list(value))

persons = [
    {"name": "Tom", "age": 25},
    {"name": "Frank", "age": 35},
    {"name": "John", "age": 25}
]
persons.sort(key=itemgetter("age"))
group_obj3 = groupby(persons, key=lambda x: x["age"])
for key, value in group_obj3:
    print(key, list(value))

# infinte loop
from itertools import count, cycle, repeat

# it goes forever if no break
for i in count(10):
    print(i)
    if i == 15:
        break

abba = [1, 2, 3]
for i in cycle(abba):
    print(i)

for i in repeat(1, 4):
    print(i)
