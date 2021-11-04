"""KT2."""


def switch_lasts_and_firsts(s: str) -> str:
    """
    Move last two characters to the beginning of string and first two characters to the end of string.

    When string length is smaller than 4, return reversed string.

    switch_lasts_and_firsts("ambulance") => "cebulanam"
    switch_lasts_and_firsts("firetruck") => "ckretrufi"
    switch_lasts_and_firsts("car") => "rac"

    :param s:
    :return: modified string
    """
    if len(s) >= 4:
        last = s[-2:]
        first = s[:2]
        middle = s[2:-2]
        return last + middle + first
    else:
        return s[-1::-1]


def take_partial(text: str, leave_count: int, take_count: int) -> str:
    """
    Take only part of the string.

    Ignore first leave_count symbols, then use next take_count symbols.
    Repeat the process until the end of the string.

    The following conditions are met (you don't have to check those):
    leave_count >= 0
    take_count >= 0
    leave_count + take_count > 0

    take_partial("abcdef", 2, 3) => "cde"
    take_partial("abcdef", 0, 1) => "abcdef"
    take_partial("abcdef", 1, 0) => ""
    """
    string = ""
    leave_c = leave_count
    take_c = take_count
    for element in text:
        if leave_count > 0:
            leave_count -= 1
            continue
        elif leave_count == 0 and take_count != 0 or leave_c == 0:
            string += element
            take_count -= 1
        elif leave_count <= 0 and take_count == 0:
            leave_count = leave_c - 1
            take_count = take_c
    return string


def min_diff(nums):
    """
    Find the smallest diff between two integer numbers in the list.

    The list will have at least 2 elements.

    min_diff([1, 2, 3]) => 1
    min_diff([1, 9, 17]) => 8
    min_diff([100, 90]) => 10
    min_diff([1, 100, 1000, 1]) => 0

    :param nums: list of ints, at least 2 elements.
    :return: min diff between 2 numbers.
    """
    smallest_diff = -1
    for i, num in enumerate(nums):
        for u, other_num in enumerate(nums):
            if num - other_num >= 0 and smallest_diff == -1 and i != u:
                smallest_diff = num - other_num
            elif 0 <= num - other_num < smallest_diff and i != u:
                smallest_diff = num - other_num
    return smallest_diff


def get_symbols_by_occurrences(text: str) -> dict:
    """
    Return dict where key is the occurrence count and value is a list of corresponding symbols.

    The order of the counts and the symbols is not important.

    get_symbols_by_occurrences("hello") => {1: ['e', 'o', 'h'], 2: ['l']}
    get_symbols_by_occurrences("abcaba") => {2: ['b'], 1: ['c'], 3: ['a']}
    """
    count_dict = {}
    for element in text:
        count = text.count(element)
        if count not in count_dict:
            count_dict[count] = [element]
        else:
            if element not in count_dict[count]:
                count_dict[count].append(element)
    return count_dict
