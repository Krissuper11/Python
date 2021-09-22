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
    type_list = [string_list, int_list, float_list, list_list, tuple_list, dict_list, set_list]
    type_dict = {"string": string_list, "int": int_list, "float": float_list, "list": list_list, "tuple": tuple_list,
                 "dict": dict_list, "set": set_list}
    for element in inputs:
        element_dict = {"string": (element[0], ""), "int": (element[0], 0), "float": (element[0], 0.1),
                        "list": (element[0], []), "tuple": (element[0], ()), "dict": (element[0], {}), "set": (element[0], set())}
        type_dict[element[1]].append(element_dict[element[1]])
    for new_list in type_list:
        max_list = max(new_list)
        for i in range(max_list[0]):
            some_list.append(max_list[1])
    return some_list
