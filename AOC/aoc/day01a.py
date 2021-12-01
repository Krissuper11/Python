"""AOC Day1a."""


def count_depth(file):
    """."""
    data_list = []
    counter = 0
    with open(file) as file:
        for row in file:
            if "\n" in row:
                data_list.append(int(row[:-1]))
            else:
                data_list.append(int(row))
    for i in range(1, len(data_list)):
        if data_list[i - 1] - data_list[i] > 0:
            counter += 1
    return counter
