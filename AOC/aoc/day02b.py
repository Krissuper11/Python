"""AOC day2b."""


def count(file):
    """."""
    data_list = []
    aim = 0
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
            forward = int(element[7:])
            position += forward
            depth += aim * forward
        elif "up" in element:
            aim -= int(element[3:])
        elif "down" in element:
            aim += int(element[5:])
    return depth * position
