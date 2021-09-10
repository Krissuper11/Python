"""Math."""


def ects(ects, weeks):
    """Convert EAP to hour per week."""
    if weeks < 1:  # can't divide by zero
        return "Impossible!"
    else:
        result = ects * 26 / weeks
        if result < 168:  # 168 hours in week
            return result
        else:
            return "Impossible!"


def average(a, b, c, d):
    """Find average."""
    return (a * 1 + b * 2 + c * 3 + d * 4) / 4


def clock(a, b, c, d):
    """Convert days, hours, minutes, seconds to minutes."""
    return a * 1440 + b * 60 + c + d / 60
