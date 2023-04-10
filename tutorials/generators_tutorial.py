"""
Generators
Generators are functions that can be paused and resumed on the fly, returning an object that can be iterated over.
Unlike lists, they are lazy and thus produce items one at a time and only when asked.
So they are much more memory efficient when dealing with large datasets.
A generator is defined like a normal function but with the yield statement instead of return.
"""


def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


# this will not print 'Starting'
cd = countdown(3)

# this will print 'Starting' and the first value
print(next(cd))

# will print the next values
print(next(cd))
print(next(cd))

# you can iterate over a generator object with a for in loop
cd = countdown(3)
for x in cd:
    print(x)

# you can use it for functions that take iterables as input
cd = countdown(3)
sum_cd = sum(cd)
print(sum_cd)

cd = countdown(3)
sorted_cd = sorted(cd)
print(sorted_cd)


# Big advantage: Generators save memory!

# with a generator, no additional sequence is needed to store the numbers
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)

import sys

print(sys.getsizeof(firstn(1000000)), "bytes")


def fibonacci(limit):
    a, b = 0, 1  # first two fibonacci numbers
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(30)
# generator objects can be converted to a list (only used for printing here)
print(list(fib))

# Generator expressions
"""
Just like list comprehensions, generators can be written in the 
same syntax except with parenthesis instead of square brackets. 
Be careful not to mix them up, since generator expressions are often slower than list comprehensions because of the 
overhead of function calls (https://stackoverflow.com/questions/11964130/list-comprehension-vs-generator-expressions-weird-timeit-results/11964478#11964478)
"""

# generator expression
mygenerator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))

# list comprehension
mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist))
