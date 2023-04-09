# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter

a = "aaaabbcccccccdee"
my_counter = Counter(a)
print(my_counter)

print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common())
print(my_counter.most_common(2)[0][0])
print(list(my_counter.elements()))

# similar to struct, like case class??
from collections import namedtuple

Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt)

# Similar to regular dict but remembers the order of inserted items
# NOT important as the newer version of python dict has default method for this
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

# default value if the key is not set
from collections import defaultdict

d = defaultdict(int)
d["a"] = 1
d["b"] = 2
print(d["b"])
print(d["c"])  # default value if not found which is 0 for int, empty list or empty string

# double ended queue
from collections import deque

deq = deque()
deq.append(1)
deq.append(2)
print(deq)
deq.appendleft(0)
print(deq)
deq.pop()
deq.popleft()
print(deq)

deq1 = deq.copy()
deq.clear()

deq1.extend([4, 5, 6])
deq1.extendleft([9])
print(deq1)

deq1.rotate(1)
print(deq1)