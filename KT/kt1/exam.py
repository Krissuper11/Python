"""KT1."""


def capitalize_string(s: str) -> str:
    """
    Return capitalized string. The first char is capitalized, the rest remain as they are.

    capitalize_string("abc") => "Abc"
    capitalize_string("ABc") => "ABc"
    capitalize_string("") => ""
    """
    if len(s) > 0:
        first_letter = s[0].capitalize()
        string = first_letter + s[1:]
        return string
    else:
        return ""


def has_seven(nums):
    """
    Given a list if ints, return True if the value 7 appears in the list exactly 3 times.

    And no consecutive elements have the same value.

    has_seven([1, 2, 3]) => False
    has_seven([7, 1, 7, 7]) => False
    has_seven([7, 1, 7, 1, 7]) => True
    has_seven([7, 1, 7, 1, 1, 7]) => False
    """
    counter = 0
    if len(nums) < 3:
        return False
    if nums[0] == 7:
        counter += 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return False
        if nums[i] == 7:
            counter += 1
    return counter == 3


def list_move(initial_list: list, amount: int, factor: int) -> list:
    """
    Create amount lists where elements are shifted right by factor.

    This function creates a list with amount of lists inside it.
    In each sublist, elements are shifted right by factor elements.
    factor >= 0

    list_move(["a", "b", "c"], 3, 0) => [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    list_move(["a", "b", "c"], 3, 1) => [['a', 'b', 'c'], ['c', 'a', 'b'], ['b', 'c', 'a']]
    list_move([1, 2, 3], 3, 2) => [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    list_move([1, 2, 3], 4, 1) => [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 2, 3]]
    list_move([], 3, 4) => [[], [], [], []]
    """
    final_list = []
    if len(initial_list) == 0:
        for i in range(amount):
            final_list.append([])
        return final_list
    for i in range(amount):
        factor %= len(initial_list)
        factor1 = factor * -1
        shift_list = []
        if i == 0:
            for element in initial_list:
                shift_list.append(element)
        else:
            for u in range(len(final_list[i - 1])):
                try:
                    shift_list.append(final_list[i - 1][factor1])
                except IndexError:
                    factor -= len(initial_list)
                    shift_list.append(final_list[i - 1][factor1])
                factor1 += 1
        final_list.append(shift_list)
    return final_list


def parse_call_log(call_log: str) -> dict:
    """
    Parse calling logs to find out who has been calling to whom.

    There is a process, where one person calls to another,
    then this another person call yet to another person etc.
    The log consists of several those call-chains, separated by comma (,).
    One call-chain consists of 2 or more names, separated by colon (:).

    The function should return a dict where the key is a name
    and the value is all the names the key has called to.

    Each name has to be in the list only once.
    The order of the list or the keys in the dictionary are not important.

    Input:
    - consists of 0 or more "chains"
    - chains are separated by comma (,)
    - one chain consists of 2 or more names
    - name is 1 or more symbols long
    - there are no commas nor colons in the name
    - names are separated by colon (:)

    parse_call_log("") => {}
    parse_call_log("ago:kati,mati:malle") => {"ago": ["kati"], "mati": ["malle"]}
    parse_call_log("ago:kati,ago:mati,ago:kati") => {"ago": ["kati", "mati"]}
    parse_call_log("ago:kati:mati") => {"ago": ["kati"], "kati": ["mati"]}
    parse_call_log("mati:kalle,kalle:malle:mari:juri,mari:mati") =>
    {'mati': ['kalle'], 'kalle': ['malle'], 'malle': ['mari'], 'mari': ['juri', 'mati']}

    :param call_log: the whole log as string
    :return: dictionary with call information
    """
    call_log_dict = {}
    call_log_list = call_log.split(",")
    for chain in call_log_list:
        name_list = chain.split(":")
        for i in range(1, len(name_list)):
            call_name = name_list[i - 1]
            answer_name = name_list[i]
            if call_name not in call_log_dict:
                call_log_dict[call_name] = [answer_name]
            else:
                if answer_name in call_log_dict[call_name]:
                    pass
                elif answer_name not in call_log_dict[call_name]:
                    call_log_dict[call_name].append(answer_name)
    return call_log_dict
