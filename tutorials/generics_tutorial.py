"""
A tutorial on Generics with Python typing including Variadic Generics, a feature in Python 3.11.

This tutorial will show you how to make TypeVar variables, how to use them in functions and classes

More about mypy: https://mypy.readthedocs.io/en/stable/index.html

"""

from typing import Any, Sequence, TypeVar


# Non-generic function
def first(values: Sequence, default: Any) -> Any:
    if len(values) == 0:
        return default
    return values[0]


names = ["Harry", "Barry", "Warry"]  # list[str]

first_name = first(names, "Jarry")  # first_name=Anz
print(first_name)

# Generic function

T = TypeVar("T")


def first_generic(values: Sequence[T], default: T) -> T:
    if len(values) == 0:
        return default
    return values[0]


names_2 = ["Harry", "Barry", "Warry"]  # list[str]

first_name_2 = first_generic(names_2, "John")  # str
print(first_name_2)

# Union type in python
from statistics import median as std_median


def median(values: list[int] | list[float]) -> float | int:
    return std_median(values)  # or some other calculation


m = median([1, 2, 3])  # float | int
print(m)

from typing import TypeVar

TNumber = TypeVar("TNumber", float, int)


def median2(values: list[TNumber]) -> TNumber:
    return std_median(values)  # or some other calculation


m_2 = median2([1, 2, 3])  # int
print(m_2)

# Generic class

from datetime import datetime
from typing import TypeVar, Generic
from uuid import UUID

TKey = TypeVar("TKey", int, UUID)
TValue = TypeVar("TValue")


class Record(Generic[TKey, TValue]):
    created: datetime
    key: TKey
    value: TValue

    def __init__(self, key: TKey, value: TValue):
        self.key = key
        self.value = value

    def update(self, value: TValue):
        self.value = value


record1 = Record(1, "Hello")  # Record[int, str]
record1.update("new word")  # update(value: str)
record1.update(1)  # typing error.

# Variadic Generics, a feature in Python 3.11
