"""File handling."""
import csv
import glob


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


def read_csv_file_into_list_of_dicts(filename: str) -> list:
    """
    Read csv file into list of dictionaries.

    Header line will be used for dict keys.

    Each line after header line will result in a dict inside the result list.
    Every line contains the same number of fields.

    Example:

    name,age,sex
    John,12,M
    Mary,13,F

    Header line will be used as keys for each content line.
    The result:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    If there are only header or no rows in the CSV-file,
    the result is an empty list.

    :param filename: CSV-file to read.
    :return: List of dictionaries where keys are taken from the header.
    """
    csv_list = read_csv_file(filename)
    list_of_dicts = []
    if len(csv_list) > 0:
        key_list = csv_list[0]
    for i in range(1, len(csv_list)):
        csv_dict = {}
        counter = 0
        for element in key_list:
            if counter > len(csv_list[i]) - 1:
                csv_dict[element] = "None"
                counter += 1
            elif not csv_list[i][counter][0].isalnum():
                csv_dict[element] = "None"
                counter += 1
            else:
                csv_dict[element] = csv_list[i][counter]
                counter += 1
        list_of_dicts.append(csv_dict)
    return list_of_dicts


def write_list_of_dicts_to_csv_file(filename: str, data: list) -> None:
    """
    Write list of dicts into csv file.

    Data contains a list of dictionaries.
    Dictionary key represents the field.

    Example data:
    [
      {"name": "john", "age": "23"}
      {"name": "mary", "age": "44"}
    ]
    Will become:
    name,age
    john,23
    mary,44

    The order of fields/headers is not important.
    The order of lines is important (the same as in the list).

    Example:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]
    Will become:
    name,age,town
    john,12,
    mary,,London

    Fields which are not present in one line will be empty.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    print_list = []
    if len(data) == 0:
        write_csv_file(filename, print_list)
    else:
        key_list = []
        values_list = []
        for element in data:
            for key in element.keys():
                if key not in key_list:
                    key_list.append(key)
        values_list = create_value_list(data, key_list)
        print_list.append(key_list)
        print_list += values_list
        write_csv_file(filename, print_list)


def create_value_list(data, key_list):
    """Create list with values from dictionary."""
    values_list = []
    for element in data:
        counter = 0
        value_list = []
        for key_from_list in key_list:
            if counter < len(element):
                if key_from_list == list(element)[counter]:
                    if key_from_list == "birth" and element["birth"] != "-":
                        element["birth"] = element["birth"].strftime("%d.%m.%Y")
                        value_list.append(element["birth"])
                        counter += 1
                    elif key_from_list == "death" and element["death"] != "-":
                        element["death"] = element["death"].strftime("%d.%m.%Y")
                        value_list.append(element["death"])
                        counter += 1
                    else:
                        value_list.append(element[list(element)[counter]])
                        counter += 1
                else:
                    value_list.append("")
            else:
                value_list.append("")
        values_list.append(value_list)
    return values_list


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str) -> list:
    """
    Read data from file and cast values into different datatypes.

    If a field contains only numbers, turn this into int.
    If a field contains only dates (in format dd.mm.yyyy), turn this into date.
    Otherwise the datatype is string (default by csv reader).

    Example:
    name,age
    john,11
    mary,14

    Becomes ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]

    But if all the fields cannot be cast to int, the field is left to string.
    Example:
    name,age
    john,11
    mary,14
    ago,unknown

    Becomes ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]

    Example:
    name,date
    john,01.01.2020
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': datetime.date(2020, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    Value "-" indicates missing value and should be None in the result
    Example:
    name,date
    john,-
    mary,01.01.2020

    Becomes:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    None value also doesn't affect the data type
    (the column will have the type based on the existing values).

    For date, strptime can be used:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date
    """
    from datetime import datetime
    list_of_dicts = read_csv_file_into_list_of_dicts(filename)
    removed_lists = removed_elements(list_of_dicts)
    removed_list_digits = removed_lists[0]
    removed_list_dates = removed_lists[1]

    for dictionary in list_of_dicts:
        for key, value in dictionary.items():
            if key not in removed_list_digits and value != "None":
                dictionary[key] = int(value)
            if key not in removed_list_dates and value != "None":
                dictionary[key] = datetime.strptime(value, "%d.%m.%Y").date()
            if value == "None":
                dictionary[key] = None

    return list_of_dicts


def removed_elements(list_of_dicts: list):
    """Check keys that are not date and int."""
    from datetime import datetime
    removed_list_dates = []
    removed_list_digits = []
    for dictionary in list_of_dicts:
        for key, value in dictionary.items():
            if not value.isdigit() and value != "None":
                removed_list_digits.append(key)
            if value != "None":
                try:
                    datetime.strptime(value, "%d.%m.%Y")
                except ValueError:
                    removed_list_dates.append(key)
    return removed_list_digits, removed_list_dates


def read_people_data(directory: str) -> dict:
    """
    Read people data from files.

    Files are inside directory. Read all *.csv files.

    Each file has an int field "id" which should be used to merge information.

    The result should be one dict where the key is id (int) and value is
    a dict of all the different values across the the files.
    Missing keys should be in every dictionary.
    Missing value is represented as None.

    File: a.csv
    id,name
    1,john
    2,mary
    3,john

    File: births.csv
    id,birth
    1,01.01.2001
    2,05.06.1990

    File: deaths.csv
    id,death
    2,01.02.2020
    1,-

    Becomes:
    {
        1: {"id": 1, "name": "john", "birth": datetime.date(2001, 1, 1), "death": None},
        2: {"id": 2, "name": "mary", "birth": datetime.date(1990, 6, 5),
            "death": datetime.date(2020, 2, 1)},
        3: {"id": 3, "name": "john", "birth": None, "death": None},
    }


    :param directory: Directory where the csv files are.
    :return: Dictionary with id as keys and data dictionaries as values.
    """
    list_with_dicts = []
    collected_data = {}
    name_in_key = False
    birth_in_key = False
    for file in glob.glob(directory + "/*.csv"):
        list_with_dicts += (read_csv_file_into_list_of_dicts_using_datatypes(file))
    for i, dictionary in enumerate(list_with_dicts):
        id_num = dictionary["id"]
        for key, value in dictionary.items():
            if key == "name":
                name_in_key = True
            if key == "birth":
                birth_in_key = True
            if key == "id" and id_num not in collected_data:
                collected_data[id_num] = []
                collected_data[id_num].append({"id": id_num})
            if key != "id":
                collected_data[id_num].append({key: value})
    check_for_none(collected_data, name_in_key, birth_in_key)
    return create_dict(collected_data)


def create_dict(collected_data):
    """Create people_data dictionary."""
    people_data = {}
    for key, value in collected_data.items():
        for i in range(len(value)):
            if key in people_data:
                people_data[key].update(value[i])
            if key not in people_data:
                people_data[key] = value[i]
    return people_data


def check_for_none(collected_data, name_in_key, birth_in_key):
    """Change from string to None if value is None."""
    for key, value in collected_data.items():
        check_name(value, name_in_key)
        check_birth(value, birth_in_key)
    return collected_data


def check_name(value, name_in_key):
    """Change from string to None if name not given."""
    if name_in_key:
        try:
            if "name" not in value[1]:
                value.insert(1, {"name": None})
        except IndexError:
            value.insert(1, {"name": None})
    return value


def check_birth(value, birth_in_key):
    """Change from string to None if birth not given."""
    if birth_in_key:
        try:
            if "birth" not in value[2]:
                value.insert(2, {"birth": None})
        except IndexError:
            value.insert(2, {"birth": None})
    return value


def generate_people_report(person_data_directory: str, report_filename: str) -> None:
    """
    Generate report about people data.

    Data should be read using read_people_data().

    The input files contain fields "birth" and "death" which are dates. Those can be in different files. There are no duplicate headers in the files (except for the "id").

    The report is a CSV file where all the fields are written to
    (along with the headers).
    In addition, there should be two fields:
    - "status" this is either "dead" or "alive" depending on whether
    there is a death date
    - "age" - current age or the age when dying.
    The age is calculated as full years.
    Birth 01.01.1940, death 01.01.2020 - age: 80
    Birth 02.01.1940, death 01.01.2020 - age: 79

    If there is no birth date, then the age is -1.

    When calculating age, dates can be compared.

    The lines in the files should be ordered:
    - first by the age ascending (younger before older);
      if the age cannot be calculated, then those lines will come last
    - if the age is the same, then those lines should be ordered
      by birthdate descending (newer birth before older birth)
    - if both the age and birth date are the same,
      then by name ascending (a before b).
    - if the names are the same or name field is missing,
      order by id ascending.

    Dates in the report should in the format: dd.mm.yyyy
    (2-digit day, 2-digit month, 4-digit year).

    :param person_data_directory: Directory of input data.
    :param report_filename: Output file.
    :return: None
    """
    from datetime import date
    people_data = read_people_data(person_data_directory)
    people_data_list = []
    today = date.today()
    for key in people_data.keys():
        age = 0
        new_dict = {"id": key}
        for element, value in people_data[key].items():
            if element == "name" and value is None:
                new_dict[element] = ""
            elif value is None:
                new_dict[element] = "-"
            else:
                new_dict[element] = value

            if "birth" not in people_data[key] or people_data[key]["birth"] is None:
                age = -1
            if element == "death" and value is None or "death" not in people_data[key]:
                new_dict["status"] = "alive"
                if age != -1:
                    age = today.year\
                        - people_data[key]["birth"].year\
                        - ((today.month, today.day)
                            < (people_data[key]["birth"].month,
                                people_data[key]["birth"].day))
            elif element == "death" and value is not None:
                new_dict["status"] = "dead"
                if age != -1:
                    age = people_data[key]["death"].year\
                        - people_data[key]["birth"].year\
                        - ((people_data[key]["death"].month,
                            people_data[key]["death"].day)
                            < (people_data[key]["birth"].month,
                                people_data[key]["birth"].day))

        new_dict["age"] = age
        people_data_list.append(new_dict)
    people_data_list = sort_list(people_data_list)
    write_list_of_dicts_to_csv_file(report_filename, people_data_list)


def sort_list(people_data_list):
    """Sort people data list."""
    max_age = 0
    for dictionary in people_data_list:
        if "birth" not in dictionary:
            birth_in_dictionary = False
        elif "birth" in dictionary:
            birth_in_dictionary = True
        if dictionary["age"] > max_age:
            max_age = dictionary["age"]
    people_data_list_new = sorted(people_data_list, key=lambda x: (
        x["age"] if x["age"] != -1 else max_age + 1,
        int(x["birth"].strftime("%m")) * -1 if birth_in_dictionary and x["birth"] != "-" else 0,
        int(x["birth"].strftime("%d")) * -1 if birth_in_dictionary and x["birth"] != "-" else 0,
        x["name"] if "name" in x else "",
        x["id"]))
    return people_data_list_new
