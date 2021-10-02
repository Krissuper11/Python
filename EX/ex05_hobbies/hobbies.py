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
    Find most popular name or hobby.

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
    Find least popular name or hobby.

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


print(find_people_with_least_hobbies(
    """Jack:crafting\nPeter:hiking\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""))
