# lambda a arguments: expression
# Used as higher order function
# Used for the method like map, filter, sort, reduce
from functools import reduce

add10 = lambda x: x + 10
print(add10(5))

mult = lambda x, y: x * y
print(mult(2, 5))

points2D = [(1, 3), (15, 1), (5, -1), (9, 0)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted)

points2D_sum = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D_sum)

my_list = [1, 2, 3, 4, 5]
list_mult = map(lambda x: x * 2, my_list)
print(list(list_mult))

list_mult_2 = [x * 2 for x in my_list]
print(list_mult_2)

filter_list = filter(lambda x: x % 2 == 0, my_list)
print(list(filter_list))

filter_list_2 = [x for x in my_list if x % 2 == 0]
print(filter_list_2)

reduce_filter = reduce(lambda x, y: x * y, my_list)
print(reduce_filter)
