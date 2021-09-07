"""Primes identifier."""


def is_prime_number(number: int) -> bool:
    number_list = [5, 7, 3, 2]
    for element in number_list:
        if number % element != 0 or number == element:
            continue
        elif number % element == 0:
            return False
    return True


print(is_prime_number(49))
