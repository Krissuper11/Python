"""File handling."""
import csv


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(filename) as file:
        data = file.read()
    return data


def read_file_contents_to_list(filename: str) -> list:
    """
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.

    List elements should not contain new line.

    :param filename: File to read.
    :return: List of lines.
    """
    with open(filename) as file:
        data_list = file.readlines()
    for i in range(len(data_list)):
        if "\n" in data_list[i]:
            data_list[i] = data_list[i][:-1]
    return data_list


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    import csv
    row_list = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            row_list.append(row)
    return row_list


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file exists, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, "w") as file:
        file.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(filename, "w") as file:
        for line in lines:
            if line == lines[len(lines) - 1]:
                file.write(line)
            else:
                file.write(f"{line}\n")


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        for row in data:
            csv_writer.writerow(row)


def merge_dates_and_towns_into_csv(dates_file: str, towns_file: str, csv_output: str) -> None:
    """
    Merge information from two files into one CSV file.

    dates_file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    towns_file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_file: Input file with names and dates.
    :param towns_file: Input file with names and towns.
    :param csv_output: Output CSV-file with names, towns and dates.
    :return: None
    """
    person_dict = {}
    person_list = []
    dates_list = read_file_contents_to_list(dates_file)
    towns_list = read_file_contents_to_list(towns_file)
    for line in dates_list:
        if ":" in line:
            index = line.find(":")
            person_dict[line[:index]] = [(line[index + 1:])]
        else:
            person_dict[line] = ["-"]
    for line in towns_list:
        if ":" in line:
            index = line.find(":")
            if line[:index] in person_dict:
                person_dict[line[:index]].insert(0, line[index + 1:])
            else:
                person_dict[line[:index]] = [(line[index + 1:]), "-"]
        else:
            person_dict[line].insert(0, "-")
    for key, value in person_dict.items():
        if len(value) < 2:
            value.insert(0, "-")
        person_list.append([key, value[0], value[1]])
    with open(csv_output, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow(["name", "town", "date"])
        for row in person_list:
            csv_writer.writerow(row)
print(merge_dates_and_towns_into_csv("C:/Users/krist/Downloads/dates.txt", "C:/Users/krist/Downloads/towns.txt", "C:/Users/krist/Downloads/test.txt"))