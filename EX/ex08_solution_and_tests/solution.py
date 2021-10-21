"""Ex08 solution."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if 18 <= time <= 24:
        return True
    elif 5 <= time <= 17:
        return coffee_needed is True
    elif 1 <= time <= 4:
        return False
    else:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == 5 and b == 5 and c == 5:
        return 10
    elif a == b == c:
        return 5
    elif a != b and a != c:
        return 1
    elif a == b or a == c:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    if ordered_amount < 0:
        return 0
    if small_baskets + big_baskets * 5 == ordered_amount:
        return small_baskets
    elif big_baskets * 5 + small_baskets < ordered_amount and big_baskets >= 0:
        return -1
    else:
        big_baskets_needed = ordered_amount // 5
        if big_baskets_needed <= big_baskets:
            ordered_amount = ordered_amount - 5 * big_baskets_needed
        if big_baskets_needed > big_baskets >= 0:
            ordered_amount = ordered_amount - 5 * big_baskets
        if small_baskets < ordered_amount:
            return -1
        else:
            return ordered_amount

