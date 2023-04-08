import sys

print("Welcome to Python tutorial for tuples collection!!")

# Tuples: ordered, immutable, allows duplicate elements

mytuple = ("Max", 20, False, "London")
mytuple_2 = "Max", 20, False, "London"  # brackets are optional

mytuple_not = ("Max")  # NOTE: this is not tuple, this is string
mytuple_3 = ("Max",)  # Add comma at the end to make it tuple

mytuple_4 = tuple(["Max", 20, False, "London"])  # from iterable
item = mytuple_4[0]
last_item = mytuple_4[-1]
print(item)

# mytuple_4[0] = "Tim"  # Error as tuple is immutable

for i in mytuple_4:
    print(i)

if "Max" in mytuple_4:
    print("Yes")
else:
    print("No")

my_tuple = ("a", "b", "c", "d", "e")
print(len(my_tuple))
print(my_tuple.count("a"))
print(my_tuple.index("d"))

my_list = list(my_tuple)  # to list
my_tuple_2 = tuple(my_list)  # to tuple

my_tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
get_items = my_tuple1[2:5]
print(get_items)  # last index is not included
print(my_tuple1[:5])
print(my_tuple1[5:])
print(my_tuple1[::2])
print(my_tuple1[::-1])  # reverse the order

mytuple_5 = ("John", 28, "London")
name, age, city = mytuple_5  # variable name should match the length
print(age, name, city)

i1, *i2, i3 = my_tuple1
print(i1)
print(i2)
print(i3)

# list vs tuples
tuple_ex = (0, 1, 2, 3, "hello", True)
list_ex = [0, 1, 2, 3, "hello", True]
print(sys.getsizeof(tuple_ex), "bytes")
print(sys.getsizeof(list_ex), "bytes")
# NOTE: list have bigger number of size

import timeit

print(timeit.timeit(stmt="[1,2,3,4]", number=100))
print(timeit.timeit(stmt="(1,2,3,4)", number=100))

# NOTE: list takes longer time

# Hence use tuples as it is more efficient than list
