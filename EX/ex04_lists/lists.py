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
    string_list = [(0, "")]
    int_list = [(0, 0)]
    float_list = [(0, 0.1)]
    list_list = [(0, [])]
    tuple_list = [(0, ())]
    dict_list = [(0, {})]
    set_list = [(0, {})]
    type_dict = {"string": string_list, "int": int_list, "float": float_list, "list": list_list, "tuple": tuple_list, "dict": dict_list, "set": set_list}
    for element in inputs:
        type_dict[element[1]].append(element)
    string_list = max(string_list)
    for i in range(string_list[0]):
        some_list.append(string_list[1])
    int_list = max(int_list)
    for i in range(int_list[0]):
        some_list.append(int_list[1])
    float_list = max(float_list)
    for i in range(float_list[0]):
        some_list.append(float_list[1])
    list_list = max(list_list)
    for i in range(list_list[0]):
        some_list.append(list_list[1])
    tuple_list = max(tuple_list)
    for i in range(tuple_list[0]):
        some_list.append(tuple_list[1])
    dict_list = max(dict_list)
    for i in range(dict_list[0]):
        some_list.append(dict_list[1])
    set_list = max(set_list)
    for i in range(set_list[0]):
        some_list.append(set_list[1])
    return some_list
