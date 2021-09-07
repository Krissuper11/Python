"""Primes identifier."""


def is_prime_number(number: int) -> bool:
    number_list = [5, 7, 3, 2]
    for element in number_list:
        if (number % element != 0 or number == element) and number != 1:
            continue
        else:
            return False
    return True
