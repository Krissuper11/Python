"""KT0."""


def add_char_into_pos(char: str, pos: int, string: str) -> str:
    """
    Return a string where a given character is added into a given position in a string.

    In the case of empty string and position 1, return the given character.

    add_char_into_pos("a", 2, "kheksa") -> "kaheksa"
    add_char_into_pos("t", 8, "kaheksa") -> "kaheksat"
    add_char_into_pos("a", 1, "mps") -> "amps"
    add_char_into_pos("a", 1, "") -> "a"
    add_char_into_pos("k", 10, "kalla") -> "kalla"

    """
    string_list = []
    result_string = ""
    for i in range(len(string)):
        string_list.append(string[i])
    if pos < len(string) + 2:
        string_list.insert(pos - 1, char)
    for element in string_list:
        result_string += element
    return result_string


def nr_of_common_characters(string1: str, string2: str) -> int:
    """
    Return a number of common characters of string1 and string2.

    Do not take into account repeated characters.

    common_characters("iva", "avis") -> 3 # 'a', 'i', 'v' are common
    common_characters("saali", "pall") -> 2  # 'a', 'l' are common
    common_characters("memm", "taat") -> 0
    common_characters("memm", "") -> 0

    """
    string1_list = []
    string2_list = []
    common_characters = []
    for i in range(len(string1)):
        string1_list.append(string1[i])
    for i in range(len(string2)):
        string2_list.append(string2[i])
    for element in string1:
        if element in string2 and element not in common_characters:
            common_characters.append(element)
    return len(common_characters)


def nr_into_num_list(nr: int, num_list: list) -> list:
    """
    Return a list of numbers where the "nr" is added into the "num_list" so that the list keep going to be sorted.

    Built-in sort methods are not allowed.

    nr_into_num_list(5, []) -> [5]
    nr_into_num_list(5, [1,2,3,4]) -> [1,2,3,4,5]
    nr_into_num_list(5, [1,2,3,4,5,6]) -> [1,2,3,4,5,5,6]
    nr_into_num_list(0, [1,2,3,4,5]) -> [0,1,2,3,4,5,]

    """
    if len(num_list) == 0:
        return [nr]
    elif nr < num_list[0] or num_list[0] == nr:
        num_list.insert(0, nr)
    elif nr > num_list[len(num_list) - 1] or nr == num_list[len(num_list) - 1]:
        num_list.append(nr)
    else:
        for i in range(1, len(num_list)):
            if nr < num_list[i]:
                num_list.insert(i, nr)
                break
    return num_list


def symbol_average_position_in_words(words):
    """
    Find the average position for each symbol.

    For the given text (list of words) the function has to find
    the average position for each symbol.

    If the list is: ["hello", "world"]
    then the positions for the symbols are:
    h: 0 (in the first word only)
    e: 1
    l: 2, 3, 3 (2, 3 in the first word, 3 in the second)
    o: 4, 1
    w: 0
    r: 2
    d: 4

    The average positions:
    h: 0
    e: 1
    l: 2.67
    o: 2.5
    w: 0
    r: 2
    d: 4
    Positions should be rounded to 2 places after the decimal point.

    The order of the keys in the dictionary is not important.

    symbol_average_position_in_words(["hello", "world"]) =>
    {'h': 0.0, 'e': 1.0, 'l': 2.67, 'o': 2.5, 'w': 0.0, 'r': 2.0, 'd': 4.0}

    symbol_average_position_in_words(["abc", "a", "bc", ""]) =>
    {'a': 0.0, 'b': 0.5, 'c': 1.5}

    symbol_average_position_in_words(["1", "a", "A"]) =>
    {'1': 0.0, 'a': 0.0, 'A': 0.0}

    :param words: list of words
    :return: dictionary with symbol average positions
    """
    result_dict = {}
    for element in words:
        for i, letter in enumerate(element):
            if letter not in result_dict:
                result_dict[letter] = [i]
            else:
                result_dict[letter].append(i)
    for key, value in result_dict.items():
        pos_sum = 0
        for pos in value:
            pos_sum += pos
        pos_average = round(pos_sum / len(value), 2)
        result_dict[key] = pos_average
    return result_dict
