"""Operators."""


def add(x, y):
    """Add x to y."""
    return x + y


def sub(x, y):
    """Subtract x to y."""
    return x - y


def multiply(x, y):
    """Subtract x from y"""
    return x * y


def divide(x, y):
    return x / y


def modulus(x, y):
    return x % y


def floor_div(x, y):
    return x // y


def exponent(x, y):
    return x ** y


def first_greater_or_equal(x, y):
    return x >= y


def second_less_or_equal(x, y):
    return y <= x


def x_is_y(x, y):
    return x == y


def x_is_not_y(x, y):
    return x != y


def if_else(a, b, c, d):
    num1 = a * b
    num2 = c / d
    if (num1 > num2) or (num1 < num2):
        return (num1 > num2) or (num1 < num2)
    elif num1 == num2:
        return 0


def surface(a, b):
    result = a * b
    return result


def volume(a, b, c):
    result = a * b * c
    return result
