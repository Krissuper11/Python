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
    some_list = []
    type_dict = {"string": "a", "int": 0, "float": 0.1, "list": [], "tuple": (), "dict": {}, "set": set()}
    for element in inputs:
        counter = 0
        while counter < element[0]:
            some_list.append(type_dict[f"{element[1]}"])
            counter += 1
    return some_list
