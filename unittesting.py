def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiple(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("can't divided by zero")
    return x / y

# print(divide(9,3))