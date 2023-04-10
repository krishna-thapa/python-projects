# The random module

"""
This module implements pseudo-random number generators for various distributions.
It uses the Mersenne Twister algorithm (https://en.wikipedia.org/wiki/Mersenne_Twister) as its core generator.
It is called pseudo-random, because the numbers seem random, but are reproducable.
"""

import random

# random float in [0,1)
a = random.random()
print(a)

# random float in range [a,b]
a = random.uniform(1, 10)
print(a)

# random integer in range [a,b]. b is included
a = random.randint(1, 10)
print(a)

# random integer in range [a,b). b is excluded
a = random.randrange(1, 10)
print(a)

# random float from a normal distribution with mu and sigma
a = random.normalvariate(0, 1)
print(a)

# choose a random element from a sequence
a = random.choice(list("ABCDEFGHI"))
print(a)

# choose k unique random elements from a sequence
a = random.sample(list("ABCDEFGHI"), 3)
print(a)

# choose k elements with replacement, and return k sized list
a = random.choices(list("ABCDEFGHI"), k=3)
print(a)

# shuffle list in place
a = list("ABCDEFGHI")
random.shuffle(a)
print(a)

# The seed generator
"""
make results reproducible, and the chain of calls after random.seed() will produce the same trail of data. 
"""

random.seed(1)
print(random.random())
print(random.uniform(1, 10))

print('\nRe-seeding with 1...\n')
random.seed(1)  # Re-seed
print(random.random())
print(random.uniform(1, 10))

# The secrets module
"""
The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as 
passwords, account authentication, security tokens, and related secrets.
"""

import secrets

# random integer in range [0, n).
a = secrets.randbelow(10)
print(a)

# return an integer with k random bits.
a = secrets.randbits(5)
print(a)

# choose a random element from a sequence
a = secrets.choice(list("ABCDEFGHI"))
print(a)
