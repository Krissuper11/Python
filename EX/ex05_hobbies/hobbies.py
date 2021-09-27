"""Hobbies."""


def create_dictionary(data):
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param data: given string from database
    :return: dictionary where keys are people and values are lists of hobbies
    """
    hobby_list = data.split("\n")
    hobby_dict = {}
    for element in hobby_list:
        index = element.index(":")
        if element[:index] in hobby_dict and element[index + 1:] not in hobby_dict[element[:index]]:
            hobby_dict[element[:index]].append(element[index + 1:])
        elif element[:index] not in hobby_dict:
            hobby_dict[element[:index]] = [element[index + 1:]]
    return hobby_dict


def sort_dictionary(dic: dict) -> dict:
    """
    Sort dictionary values alphabetically.

    The order of keys is not important.

    :param dic: dictionary to sort
    :return: sorted dictionary
    """
    for key in dic:
        dic[key] = sorted(dic[key])
    return dic
