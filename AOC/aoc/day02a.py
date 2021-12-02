"""AOC day2a."""


def count(file):
    """."""
    data_list = []
    depth = 0
    position = 0
    with open(file) as file:
        for row in file:
            if "\n" in row:
                data_list.append(row[:-1])
            else:
                data_list.append(row)
    for element in data_list:
        if "forward" in element:
            position += int(element[7:])
        elif "up" in element:
            depth -= int(element[3:])
        elif "down" in element:
            depth += int(element[5:])
    return depth * position
