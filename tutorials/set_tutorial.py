# Sets: unordered, mutable and no duplicates

myset = {1, 2, 3, 4, 5}
print(myset)
# list to set
myset2 = set([1, 2, 3, 4, 5])
print(myset2)
# string to set
myset3 = set("Hello")
print(myset3)
# empty set
myset4 = set()

myset4.add(1)
myset4.add(2)
myset4.add(3)
myset4.add(4)

myset4.remove(4)
myset4.discard(5)  # No exception if item not found
print(myset4)
myset3.pop()
myset3.clear()

for i in myset4:
    print(i)

if "3" in myset4:
    print("yes")
else:
    print("No")

# Union, diff, intersect
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

unions = odds.union(evens)
print(unions)

intersect = odds.intersection(evens)
print(intersect)

diff1 = odds.difference(primes)
print(diff1)

diff2 = odds.symmetric_difference(primes)
print(diff2)

odds.update(evens)
print(odds)

odds.intersection_update(primes)
print(odds)

odds.difference_update(evens)
print(odds)

odds.symmetric_difference_update(evens)
print(odds)

setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3}

print(setA.issuperset(setB))
print(setB.issubset(setA))

# If the set doesn't contain any matched item
print(setB.isdisjoint({7, 8, 9}))

# NOTE: If you modify the copied, then original also get modified
# setA = setB

# To copy, use
setA = setB.copy()
setA2 = set(setB)

# Update, add, remove won't work but union, diff and intersect will work
immutable_set = frozenset([1,2,3,4,5])
print(immutable_set)
