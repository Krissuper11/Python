"""List and tuple."""


def generate_list(amount: int, data_type: str):
    """Return a list with amount elements of type data_type."""
    import random
    some_list = []
    if data_type == "int":
        data_type = random.randint(0, 9)
    elif data_type == "string":
        data_type = "a"
    elif data_type == "float":
        data_type = 0.1
    elif data_type == "list":
        data_type = []
    elif data_type == "tuple":
        data_type = ()
    elif data_type == "dict":
        data_type = {}
    elif data_type == "set":
        data_type = set()
    for i in range(amount):
        some_list.append(data_type)
    return some_list


def generate_combined_list(inputs: list):
    """
    A function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains at least 'amount' of elements of type
    'data_type'.
    """
    some_list = []
    string_list = []
    int_list = []
    float_list = []
    list_list = []
    tuple_list = []
    dict_list = []
    set_list = []
    type_dict = {"string": string_list, "int": int_list, "float": float_list, "list": list_list, "tuple": tuple_list,
                 "dict": dict_list, "set": set_list}
    for element in inputs:
        amount = element[0]
        data_type = element[1]
        element_dict = {"string": "", "int": 0, "float": 0.1, "list": [], "tuple": (), "dict": {}, "set": set()}
        if amount > len(type_dict[data_type]):
            add_num = amount - len(type_dict[data_type])
            for i in range(add_num):
                type_dict[data_type].append(element_dict[data_type])
                some_list.append(element_dict[data_type])

    return some_list


def generate_combined_list_unique(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains at least 'amount' of elements of type 'data_type'.
    Data types used in this function are 'int', 'float' and 'str' (string).
    The returned list can contain only unique elements.
    """
    some_list = []
    string_list = []
    int_list = []
    float_list = []
    type_dict = {"string": string_list, "int": int_list, "float": float_list}
    int_counter = 1
    float_counter = 0.11
    for element in inputs:
        amount = element[0]
        data_type = element[1]
        if amount > len(type_dict[data_type]):
            add_num = amount - len(type_dict[data_type])
            for i in range(add_num):
                element_dict = {"string": chr(int_counter), "int": int_counter, "float": float_counter}
                type_dict[data_type].append(element_dict[data_type])
                some_list.append(element_dict[data_type])
                if data_type == "int" or data_type == "string":
                    int_counter += 1
                elif data_type == "float":
                    float_counter += 0.1
    return some_list
