# Decorators
"""
A decorator is a function that takes another function and extends the behavior of this function
without explicitly modifying it.
It is a very powerful tool that allows to add new functionality to an existing function.
There are 2 kinds of decorators:

1. Function decoratos
2. Class decorators
"""


def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')

    return wrapper


@start_end_decorator
def print_name():
    print('Alex')


print_name()


def start_end_decorator_2(func):
    def wrapper(*args, **kwargs):
        print('Start')
        result_inside = func(*args, **kwargs)
        print('End')
        return result_inside

    return wrapper


@start_end_decorator_2
def add_5(x):
    return x + 5


result = add_5(10)
print(add_5.__name__)
print(result)

"""
use the functools.wraps decorator, which will preserve the information about the original function. 
This is helpful for introspection purposes, i.e. the ability of an object to know about its own attributes at runtime
"""

import functools


def start_end_decorator_4(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result_inside = func(*args, **kwargs)
        print('End')
        return result_inside

    return wrapper


@start_end_decorator_4
def add_5(x):
    return x + 5


result = add_5(10)
print(result)
print(add_5.__name__)
help(add_5)


# The final template for own decorators
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result

    return wrapper


"""
Nested Decorators
We can apply several decorators to a function by stacking them on top of each other. 
The decorators are being executed in the order they are listed.
"""


# a decorator function that prints debug information about the wrapped function
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result

    return wrapper


@debug
@start_end_decorator_4
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting


# now `debug` is executed first and calls `@start_end_decorator_4`, which then calls `say_hello`
say_hello(name='Alex')

# Class decorators
"""
Class decorators are typically used to maintain a state, e.g. here we keep track of the number of times our function 
is executed. It adds some functionality, executes the function, and returns its result
"""


class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello(num):
    print("Hello!")


say_hello(5)
say_hello(5)
