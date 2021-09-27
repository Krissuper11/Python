"""TK 1."""


def format_time(minutes: int) -> str:
    """
    Given minutes as an int, return correctly formatted time in hours and minutes.

    :param minutes: given minutes.
    :return: formatted time in hours and minutes.
    """
    hours = minutes // 60
    minutes -= hours * 60
    if hours == 0:
        return f"{minutes}min"
    elif minutes == 0:
        return f"{hours}h"
    else:
        return f"{hours}h {minutes}min"


def lucky_guess(n: int) -> bool:
    """
    Determine whether the given number gives you points for this task or not.

    The number gives you points if it is:
    * either 1, 3 or 7
    * greater or equal than -6 and smaller or equals than 121 and
      divisible by 13 (-6 and 121 are inclusive)
    * smaller than 0 and does not contain number 5 or 6

    :param n: given number.
    :return: boolean - points or no points.
    """
    return (n in (1, 3, 7)) or (-6 <= n <= 121 and n % 13 == 0) or (n < 0 and "5" not in str(n) and "6" not in str(n))


def sum_of_a_beach(s: str) -> int:
    """
    Count how many beach elements are in the string.

    Beaches are filled with sand, water, fish, and sun.
    Given a string, calculate how many times the words
    “Sand”, “Water”, “Fish”, and “Sun” appear without
    overlapping (regardless of the case).
    """
    s = s.lower()
    counter = 0
    counter += s.count("fish")
    counter += s.count("water")
    counter += s.count("sun")
    counter += s.count("sand")
    return counter


def index_index_value(nums: list) -> int:
    """
    Return value at index.

    Take the last element.
    Use the last element value as the index to get another value.
    Use this another value as the index of yet another value.
    Return this yet another value.

    If the the last element points to out of list, return -1.
    If the element at the index of last element points out of the list, return -2.

    All elements in the list are non-negative.

    :param nums: List of integer.
    :return: Value at index of value at index of last element's value.
    """
    first_index = nums[len(nums) - 1]
    if first_index > len(nums) - 1:
        return -1
    else:
        second_index = nums[first_index]
        if second_index > len(nums) - 1:
            return -2
        else:
            return nums[second_index]


def word_numeration(words: list) -> list:
    """
    For a given list of string, add numeration for every string.

    The input list consists of strings. For every element in the input list,
    the output list adds a numeration after the string.
    The format is as follows: #N, where N starts from 1.
    String comparison should be case-insensitive.
    The case of symbols in string itself in output list should remain the same as in input list.

    The output list has the same amount of elements as the input list.
    For every element in the output list, "#N" is added, where N = 1, 2, 3, ...

    :param words: A list of strings.
    :return: List of string with numeration.
    """
    word_dict = {}
    new_list = []
    for element in words:
        lowercase_element = element.lower()
        if lowercase_element in word_dict:
            word_dict[lowercase_element] += 1
        else:
            word_dict[lowercase_element] = 1
        new_list.append(f"{element}#{word_dict[lowercase_element]}")
    return new_list
