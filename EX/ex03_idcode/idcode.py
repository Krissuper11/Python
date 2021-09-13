"""Personal code."""


def find_id_code(text: str) -> str:
    """Check for numbers and length."""
    id_code = ""
    for i in range(len(text)):
        if text[i].isdigit():
            id_code += text[i]
        else:
            id_code += ""
    if len(id_code) < 11:
        return "Not enough numbers!"
    elif len(id_code) > 11:
        return "Too many numbers!"
    elif len(id_code) == 11:
        return id_code


def is_valid_gender_number(first_number: int) -> bool:
    """Check for valid gender number."""
    if first_number == 0 or first_number > 6:
        return False
    else:
        return True


def get_gender(first_number: int):
    """Check for valid gender number."""
    if first_number % 2 == 0 and 0 < first_number <= 6:
        return "female"
    elif first_number % 2 != 0 and 0 < first_number <= 5:
        return "male"
    else:
        return False


def is_valid_year_number(year_number: int):
    """Check for valid year number."""
    if 0 <= year_number <= 99:
        return True
    else:
        return False


def is_valid_month_number(month_number: int):
    """Check for valid month number."""
    if 0 < month_number <= 12:
        return True
    else:
        return False


def is_valid_birth_number(birth_number: int):
    """Check for valid birth number."""
    if 0 < birth_number <= 999:
        return True
    else:
        return False


def is_leap_year(year_number):
    """Check for leap year."""
    if year_number % 4 == 0 and year_number % 100 != 0:
        return True
    elif year_number % 400 == 0:
        return True
    else:
        return False


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
