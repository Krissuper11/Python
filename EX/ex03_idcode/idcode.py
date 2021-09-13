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
    if 0 <= birth_number <= 999:
        return True
    else:
        return False
