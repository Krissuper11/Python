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


def create_dictionary_with_hobbies(data: str) -> dict:
    """
    Create dictionary about hobbies and their hobbyists ie. {hobby1: [name1, name2, ...], hobby2: [...]}.

    :param data: given string from database
    :return: dictionary, where keys are hobbies and values are lists of people. Values are sorted alphabetically
    """
    hobby_dict = create_dictionary(data)
    name_dict = {}
    for key, value in hobby_dict.items():
        for element in value:
            if element not in name_dict:
                name_dict[element] = [key]
            elif element in name_dict:
                name_dict[element].append(key)
    name_dict = sort_dictionary(name_dict)
    return name_dict


def find_max(hobby_dict: dict) -> list:
    """
    Create list with most popular name or hobby.

    :param hobby_dict:
    :return: list with most popular hobbies or names, sort alphabetically
    """
    counter = 0
    name_list = []
    for key, value in hobby_dict.items():
        if len(value) > counter:
            counter = len(value)
            name_list = [key]
        elif len(value) == counter:
            name_list.append(key)
    name_list.sort()
    return name_list


def find_min(hobby_dict) -> list:
    """
    Create list with least popular name or hobby.

    :param hobby_dict:
    :return: list with least popular hobbies or names, sort alphabetically
    """
    name_list = []
    counter = 1000
    for key, value in hobby_dict.items():
        if len(value) < counter:
            counter = len(value)
            name_list = [key]
        elif len(value) == counter:
            name_list.append(key)
    name_list.sort()
    return name_list


def find_people_with_most_hobbies(data: str) -> list:
    """
    Find the people who have most hobbies.

    :param data: given string from database
    :return: list of people with most hobbies. Sorted alphabetically.
    """
    hobby_dict = create_dictionary(data)
    name_list = find_max(hobby_dict)
    return name_list


def find_people_with_least_hobbies(data: str) -> list:
    """
    Find the people who have least hobbies.

    :param data: given string from database
    :return: list of people with least hobbies. Sorted alphabetically.
    """
    hobby_dict = create_dictionary(data)
    name_list = find_min(hobby_dict)
    return name_list


def find_most_popular_hobbies(data: str) -> list:
    """
    Find the most popular hobbies.

    :param data: given string from database
    :return: list of most popular hobbies. Sorted alphabetically.
    """
    hobby_dict = create_dictionary_with_hobbies(data)
    hobby_list = find_max(hobby_dict)
    return hobby_list


def find_least_popular_hobbies(data: str) -> list:
    """
    Find the people who have least hobbies.

    :param data: given string from database
    :return: list of people with least hobbies. Sorted alphabetically.
    """
    hobby_dict = create_dictionary_with_hobbies(data)
    hobby_list = find_min(hobby_dict)
    return hobby_list


def sort_names_and_hobbies(data: str) -> tuple:
    """
    Create a tuple of sorted names and their hobbies.

    The structure of the tuple is as follows:
    (
        (name1, (hobby1, hobby2)),
        (name2, (hobby1, hobby2)),
         ...
    )

    For each person, there is a tuple, where the first name is the name (string)
    and the second name is an ordered tuple of hobbies (ordered alphabetically).
    All those person-tuples are ordered by the name of the person and are inside a tuple.
    """
    hobby_dict = sort_dictionary(create_dictionary(data))
    hobby_dict_names = sorted(hobby_dict)
    hobby_list = []
    for name in hobby_dict_names:
        hobby_tuple = (name, tuple(hobby_dict[name]))
        hobby_list.append(hobby_tuple)
    person_tuple = tuple(hobby_list)
    return person_tuple
