"""ID code: check and generation."""


def find_id_code(text: str) -> str:
    """Check for numbers and length."""
    id_code = ""
    for i in text:
        if i.isdigit():
            id_code += i
        else:
            id_code += ""
    if len(id_code) < 11:
        return "Not enough numbers!"
    elif len(id_code) > 11:
        return "Too many numbers!"
    elif len(id_code) == 11:
        return id_code


def is_valid_gender_number(gender_number: int) -> bool:
    """Check for valid gender number."""
    return gender_number != 0 and gender_number < 6


def get_gender(gender_number: int):
    """Check for valid gender number."""
    if gender_number % 2 == 0 and 0 < gender_number <= 6:
        return "female"
    elif gender_number % 2 != 0 and 0 < gender_number <= 5:
        return "male"
    else:
        return False


def is_valid_year_number(year_number: int):
    """Check for valid year number."""
    return 0 <= year_number <= 99


def is_valid_month_number(month_number: int):
    """Check for valid month number."""
    return 0 < month_number <= 12


def is_valid_birth_number(birth_number: int):
    """Check for valid birth number."""
    return 0 < birth_number <= 999


def is_leap_year(year_number):
    """Check for leap year."""
    return (year_number % 4 == 0 and year_number % 100 != 0) or year_number % 400 == 0


def get_full_year(gender_number: int, year_number: int):
    """Get full year number."""
    full_year_number = 0
    if gender_number <= 2:
        full_year_number += 1800
    elif 2 < gender_number <= 4:
        full_year_number += 1900
    elif 4 < gender_number <= 6:
        full_year_number += 2000
    full_year_number += year_number
    return full_year_number


def get_birth_place(birth_number: int):
    """Get birth place by birth number."""
    if not is_valid_birth_number(birth_number):
        return "Wrong input!"
    else:
        if 0 < birth_number <= 10:
            return "Kuressaare"
        elif 10 < birth_number <= 20 or 270 < birth_number <= 370:
            return "Tartu"
        elif 20 < birth_number <= 220 or 470 < birth_number <= 710:
            return "Tallinn"
        elif 220 < birth_number <= 270:
            return "Kohtla-Järve"
        elif 370 < birth_number <= 420:
            return "Narva"
        elif 420 < birth_number <= 470:
            return "Pärnu"
        elif 710 < birth_number <= 999:
            return "undefined"


def is_valid_control_number(id_code: str):
    """Check for control number."""
    u = 0
    control_number = 0
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    list2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    for i in list1:
        control_number += int(id_code[u]) * i
        u += 1
    if control_number % 11 < 10:
        control_number %= 11
    else:
        control_number = 0
        u = 0
        for num in list2:
            control_number += int(id_code[u]) * num
            u += 1
        if control_number % 11 < 10:
            control_number %= 11
        elif control_number % 11 == 10:
            control_number = 0
    return control_number == int(id_code[10])


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int):
    """Check for valid day number."""
    year = get_full_year(gender_number, year_number)
    return (month_number in (1, 3, 5, 7, 8, 10, 12) and 0 < day_number <= 31) \
        or (month_number in (4, 6, 9, 11) and 0 < day_number < 31) \
        or (month_number == 2 and is_leap_year(year) and 0 < day_number <= 29) \
        or (month_number == 2 and 0 < day_number <= 28)


def is_id_valid(id_code: str):
    """Check if ID code is valid."""
    id_code = find_id_code(id_code)
    if not find_id_code(id_code) == "Not enough numbers!" or find_id_code(id_code) == "Too many numbers!":
        gender_number = int(id_code[0])
        year_number = int(id_code[1:3])
        month_number = int(id_code[3:5])
        day_number = int(id_code[5:7])
        birth_number = int(id_code[7:10])
        return is_valid_gender_number(gender_number) and is_valid_year_number(year_number) \
            and is_valid_control_number(id_code) and is_valid_month_number(month_number) \
            and is_valid_birth_number(birth_number) and is_valid_day_number(gender_number, year_number, month_number, day_number)


def get_data_from_id(id_code: str):
    """Get data from ID code."""
    id_code = find_id_code(id_code)
    if is_id_valid(id_code):
        gender_number = int(id_code[0])
        year_number = int(id_code[1:3])
        month_number = int(id_code[3:5])
        day_number = int(id_code[5:7])
        birth_number = int(id_code[7:10])
        return f"This is a {get_gender(gender_number)} born on {day_number:02}.{month_number:02}.{get_full_year(gender_number, year_number)} in {get_birth_place(birth_number)}."
    else:
        return "Given invalid ID code!"


def generate_id_code(seven_numbers: str, control_number: str, check_number: int = 0):
    """Generate ID code."""
    import random
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = [3, 4, 5, 6, 7, 8, 9]
    result = 0
    u = 0
    for i in list1:
        result += int(seven_numbers[u]) * i
        u += 1
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        z = random.randint(0, 9)
        result1 = (result + x * 8 + y * 9 + z) % 11
        if check_number == 0 and is_valid_control_number(seven_numbers + str(x) + str(y) + str(z) + control_number):
            id_code = seven_numbers + str(x) + str(y) + str(z) + control_number
            break
        elif check_number == 1 and result1 % 11 != 10 and is_valid_control_number(seven_numbers + str(x) + str(y) + str(z) + control_number):
            id_code = seven_numbers + str(x) + str(y) + str(z) + control_number
            break
        if (check_number == 2 or check_number == 3) and result1 == 10:
            result1 = 0
            u = 0
            for num in list2:
                result1 += int(seven_numbers[u]) * num
                u += 1
            result1 += x + y * 2 + z * 3
            if result1 % 11 == 10 and check_number == 3 and is_valid_control_number(seven_numbers + str(x) + str(y) + str(z) + control_number):
                id_code = seven_numbers + str(x) + str(y) + str(z) + control_number
                break
            elif check_number == 2 and result1 % 11 != 10 and is_valid_control_number(seven_numbers + str(x) + str(y) + str(z) + control_number):
                print(result1 % 11)
                id_code = seven_numbers + str(x) + str(y) + str(z) + control_number
                break
    return id_code
