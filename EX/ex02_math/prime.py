"""Primes identifier."""


def is_prime_number(number: int) -> bool:
    """Check if the parameter number is a prime number"""
    if number == 1 or number == 0:
        return False
    for i in range(2, number):
        if number % i != 0:
            continue
        else:
            return False
    return True
