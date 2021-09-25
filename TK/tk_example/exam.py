"""Example TK."""


def workday_count(days):
    """
    Given number of days.

    Return how many of these days are workdays.
    Workdays are first five days of the weeks, last two are not.
    Always start from the start of the week.

    :param days:
    :return: workdays in given days
    """
    counter = 1
    workdays = 0
    for i in range(days):
        if 1 <= counter <= 5:
            workdays += 1
        elif counter >= 7:
            counter -= 7
        counter += 1
    return workdays


def sorta_sum(a: int, b: int):
    """
    Given 2 ints, a and b, return their sum.

    However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

    :param a: Integer
    :param b: Integer
    :return: Sum or 20
    """
    result = a + b
    if 10 <= result <= 19:
        return 20
    else:
        return result


def extra_end(s: str) -> str:
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.

    The string length will be at least 2.

    :param s: Input string
    :return: 3 copies of last 2 chars.
    """
    if len(s) >= 2:
        return s[-2:] * 3


def last_indices_elements_sum(nums):
    """
    Return sum of elements at indices of last two elements.

    Take element at the index of the last element value
    and take element at the index of the previous element value.
    Return the sum of those two elements.

    If the index for an element is out of the list, use 0 instead.

    The list contains at least 2 elements.

    :param nums: List of non-negative integers.
    :return: Sum of elements at indices of last two elements.
    """
    first_index = nums[len(nums) - 1]
    second_index = nums[len(nums) - 2]
    if first_index > len(nums) - 1:
        first_element = 0
    else:
        first_element = nums[first_index]
    if second_index > len(nums) - 1:
        second_element = 0
    else:
        second_element = nums[second_index]
    return first_element + second_element


def divisions(numbers: list) -> int:
    """
    You are given a list of unique integers.

    Find how many pairs of numbers there are in that list, such that for each pair, one of it's members is divisible
    by the other.

    Note that "n and m" is considered the same pair as "m and n".

    :param numbers: List of integers
    :return: Amount of pairs
    """
    counter = 0
    for first_element in numbers:
        for second_element in numbers:
            if first_element != second_element and first_element % second_element == 0:
                counter += 1
    return counter
