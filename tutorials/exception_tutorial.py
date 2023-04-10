# Errors and Exception

# a = 5 print(a) # Syntax error

# a = 5 + "" # Exception

# [1,2,3].remove(9) # Value error

x = 5
if x < 0:
    raise Exception("X should be positive")

assert (x == 5), "X is not negative"

try:
    a = 5 / 0
except:
    print("an error happened")

try:
    a = 5 / 0
except Exception as e:
    print(e)

try:
    a = 5 / 0
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is fine, no exception was thrown")
finally:
    print("Always runs no matter if the exception was thrown")


class CustomExceptionError(Exception):
    pass


class CustomValueError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise CustomExceptionError("Value is too high")
    if x < 5:
        raise CustomValueError("Value is too small", x)


try:
    test_value(2)
except CustomExceptionError as e:
    print(e)
except CustomValueError as err:
    print(err.message, err.value)
