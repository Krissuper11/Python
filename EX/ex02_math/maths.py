"""Math."""


def ects(ects, weeks):
    """Convert EAP to hour per week."""
    if weeks < 1:
        return False
    else:
        result = ects * 26 / weeks
        if result < 168:  # 168 hours in week
            return result
        else:
            return "Impossible!"


print(ects(1, 0))


def average(a, b, c, d):
    """Find average."""
    result = (a * 1 + b * 2 + c * 3 + d * 4) / 4
    return result


def clock(a, b, c, d):
    """Convert days, hours, minutes, seconds to minutes."""
    result = a * 1440 + b * 60 + c + d / 60
    return result
