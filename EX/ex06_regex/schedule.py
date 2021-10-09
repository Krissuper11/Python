"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    pass


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    counter = 0
    regex_dict = {}
    schedule_dict = {}
    string_regex = re.finditer(r"((?<= )[0-2]?\d|^[0-2]?\d?)[\D]([0-5]?[0-9]) ([A-Za-zõüöäÕÜÖÄ]+)", input_string)
    for match in string_regex:
        hour = match.group(1)
        minute = match.group(2)
        task = match.group(3).lower()
        time = f"{int(hour):02}:{int(minute):02}"
        if time not in regex_dict:
            regex_dict[time] = task
        elif time in regex_dict and task not in regex_dict[time]:
            regex_dict[time] = f"{regex_dict[time]}, {task}"
    regex_dict = dict(sorted(regex_dict.items(), key=lambda x: x[0]))
    formatted_time = get_formatted_time(regex_dict)
    for value in regex_dict.values():
        if not counter > len(formatted_time) - 1:
            schedule_dict[formatted_time[counter]] = value
            counter += 1
    table = create_table(schedule_dict)
    return table


def get_formatted_time(time_list) -> list:
    """Format 24 hour time to the 12 hour time."""
    time = []
    for element in time_list:
        hour_min = element.split(":")
        hours = int(hour_min[0])
        minutes = int(hour_min[1])
        if hours == 0:
            time.append(f"12:{minutes:02} AM")
        elif hours == 12:
            time.append(f"{hours}:{minutes:02} PM")
        elif 12 < hours < 24:
            time.append(f"{hours - 12}:{minutes:02} PM")
        elif hours < 12:
            time.append(f"{hours}:{minutes:02} AM")
    return time


def get_table_sizes(schedule_dict: dict):
    """Get the maximum sizes for table."""
    key_len = 0
    value_len = 0
    for key in schedule_dict.keys():
        if len(key) > key_len:
            key_len = len(key)
    for value in schedule_dict.values():
        if len(value) > value_len:
            value_len = len(value)
    return key_len, value_len


def create_table(schedule_dict: dict):
    """Create table."""
    if len(schedule_dict) > 0:
        sizes = get_table_sizes(schedule_dict)
        if sizes[1] >= 5:
            width = sizes[0] + sizes[1]
            table = f"{'-' * (width + 7)}\n"
            table += f"| {'time':>{sizes[0]}} | {'items':{sizes[1]}} |\n"
            table += f"{'-' * (width + 7)}\n"
            for key in schedule_dict.keys():
                table += f"| {key:>{sizes[0]}} | {schedule_dict[key]:{sizes[1]}} |\n"
            table += f"{'-' * (width + 7)}\n"
        else:
            table = f"{'-' * (sizes[0] + 12)}\n"
            table += f"| {'time':>{sizes[0]}} | items |\n"
            table += f"{'-' * (sizes[0] + 12)}\n"
            for key in schedule_dict.keys():
                table += f"| {key:>{sizes[0]}} | {schedule_dict[key]:{5}} |\n"
            table += f"{'-' * (sizes[0] + 12)}\n"
    else:
        width = len("No items found")
        table = f"{'-' * (width + 4)}\n"
        table += f"|  time | items  |\n"
        table += f"{'-' * (width + 4)}\n"
        table += f"| No items found |\n"
        table += f"{'-' * (width + 4)}\n"
    return table
