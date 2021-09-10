"""Operators."""


def add(x, y):
    """Add x to y."""
    return x + y


def sub(x, y):
    """Subtract x to y."""
    return x - y


def multiply(x, y):
    """Subtract x from y."""
    return x * y


def div(x, y):
    """Divide x by y."""
    return x / y


def modulus(x, y):
    """Divide x by y and return remainder."""
    return x % y


def floor_div(x, y):
    """Divide x by y and floor the value."""
    return x // y


def exponent(x, y):
    """Calculate x where y is an exponent."""
    return x ** y


def first_greater_or_equal(x, y):
    """If x is greater or equal than y then return True. If not then return False."""
    if x >= y:
        return True
    else:
        return False


def second_less_or_equal(x, y):
    """If y is less or equal than x then return True. If not then return False."""
    if y <= x:
        return True
    else:
        return False


def x_is_y(x, y):
    """If x same as y then return True. If not then return False."""
    if x == y:
        return True
    else:
        return False


def x_is_not_y(x, y):
    """If x is not same as y then return True. If not then return False."""
    if x != y:
        return True
    else:
        return False


def if_else(a, b, c, d):
    """Multiply parameters 1-2 and divide 3-4, then check greater value."""
    num1 = a * b
    num2 = c / d
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    elif num1 == num2:
        return 0


def surface(a, b):
    """Add the missing parameters to calculate the surface. Calculate and return the value of surface."""
    return a * b


def volume(a, b, c):
    """Add the missing parameters to calculate the volume. Calculate and return the value of volume."""
    return a * b * c
