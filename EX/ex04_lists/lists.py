"""List and tuple."""


def generate_list(amount: int, data_type: str):
    """Return a list with amount elements of type data_type."""
    some_list = []
    element_dict = {"string": "", "int": 0, "float": 0.1, "list": [], "tuple": (), "dict": {}, "set": set()}
    for i in range(amount):
        some_list.append(element_dict[data_type])
    return some_list


def generate_combined_list(inputs: list):
    """
    A function that returns a lists with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned lists contains at least 'amount' of elements of type
    'data_type'.
    """
    counter = 0
    some_list = []
    string_list = [(0, "string")]
    int_list = [(0, "int")]
    float_list = [(0, "float")]
    list_list = [(0, "lists")]
    tuple_list = [(0, "tuple")]
    dict_list = [(0, "dict")]
    set_list = [(0, "set")]
    type_dict = {"string": string_list, "int": int_list, "float": float_list, "lists": list_list, "tuple": tuple_list,
                 "dict": dict_list, "set": set_list}
    type_list = [string_list, int_list, float_list, list_list, tuple_list, dict_list, set_list]
    for element in inputs:
        data_type = element[1]
        type_dict[data_type].append(element)
    for lists in type_list:
        lists = max(lists)
        amount = lists[0]
        data_type = lists[1]
        lists = generate_list(amount, data_type)
        counter += 1
        for i in range(len(lists)):
            some_list.append(lists[i])
    return some_list


def generate_combined_list_unique(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains at least 'amount' of elements of type 'data_type'.
    Data types used in this function are 'int', 'float' and 'str' (string).
    The returned list can contain only unique elements.
    """
    some_list = generate_combined_list(inputs)
    int_counter = 1
    float_counter = 0.25
    for i in range(len(some_list)):
        if some_list[i] == 0:
            some_list[i] = int_counter
            int_counter += 1
        elif some_list[i] == "":
            some_list[i] = chr(int_counter)
            int_counter += 1
        elif some_list[i] == 0.1:
            some_list[i] = float_counter
            float_counter += 0.1
    return some_list


def generate_combined_list_unique_advanced(inputs):
    """
        Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

        Every element of 'inputs' is a tuple (int amount, string data_type).
        For each element of 'inputs', it must be true that the returned list contains at least 'amount' of elements of type 'data_type'.
        All the data types from the first function are used here.
        The returned list can contain only unique elements.
        """
    some_list = []
    list_list = []
    tuple_list = []
    dict_list = []
    set_list = []
    type_dict = {"list": list_list, "tuple": tuple_list,"dict": dict_list, "set": set_list}
    int_counter = 1
    float_counter = 0.11
    for element in inputs:
        input_list = [element]
        amount = element[0]
        data_type = element[1]
        if data_type == "string" or data_type == "float" or data_type == "int":
            some_list.append(generate_combined_list_unique(input_list))
        else:
            if amount > len(type_dict[data_type]):
                add_num = amount - len(type_dict[data_type])
                for i in range(add_num):
                    element_dict = {"list": [int_counter], "tuple": (int_counter,), "dict": {int_counter: chr(int_counter)}, "set": set([float_counter])}
                    type_dict[data_type].append(element_dict[data_type])
                    some_list.append(element_dict[data_type])
                    if data_type == "list" or data_type == "tuple" or data_type == "dict":
                        int_counter += 1
                    elif data_type == "set":
                        float_counter += 0.1
    return some_list
