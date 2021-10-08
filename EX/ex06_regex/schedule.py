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
            regex_dict[time] = [task]
        elif time in regex_dict:
            regex_dict[time].append(task)
    regex_dict = dict(sorted(regex_dict.items(), key=lambda x: x[0]))
    formatted_time = get_formatted_time(regex_dict)
    for value in regex_dict.values():
        schedule_dict[formatted_time[counter]] = value
        counter += 1




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
print(get_formatted_time(['00:00', '00:12', '07:01', '08:01', '08:08', '10:00', '11:00', '18:19', '24:01']))

if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    print(create_schedule_string(
        """A 11:00 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed euismod nibh, non vehicula libero. Fusce ac eros
     lectus. Pellentesque interdum nisl sem, eget facilisis mauris malesuada eget. Nullam 10:0 a bibendum enim. Praesent dictum
     ante eget turpis tempor, porta placerat dolor ultricies. Mauris quis dui porttitor, ultrices turpis vitae, pulvinar nisl.
     Suspendisse potenti. Ut nec cursus sapien, convallis sagittis purus. Integer mollis nisi sed fermentum efficitur.
     Suspendisse sollicitudin sapien dui, vitae tempus lacus elementum ac. Curabitur id purus diam. 24:01 Donec blandit,
     est nec semper convallis, arcu libero lacinia ex, eu placerat risus est non tellus.

    Orci varius natoque penatibus et magnis dis 0:12 parturient montes, nascetur ridiculus mus. Curabitur pretium at metus
    eget euismod. Nunc sit amet fermentum urna. Maecenas commodo ex turpis, et malesuada tellus sodales non. Fusce elementum
     eros est. Phasellus nibh magna, tincidunt eget magna nec, rhoncus lobortis dui. Sed fringilla risus a justo tincidunt,
     in tincidunt urna interdum. Morbi varius lobortis tellus, vitae accumsan justo commodo in. 12:001 Nullam eu lorem leo.
     Vestibulum in varius magna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
      0:00 Aliquam ac velit sit amet nunc dictum aliquam pulvinar at enim. Nulla aliquam est quis sem laoreet, eu venenatis
      risus hendrerit. Donec ac enim lobortis, bibendum lacus quis, egestas nisi.

    08:01 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed euismod nibh, non vehicula libero. Fusce ac eros
     lectus. Pellentesque interdum nisl sem, eget facilisis mauris malesuada eget. Nullam 18:19 a bibendum enim. Praesent
     dictum ante eget turpis tempor, 00:0 porta placerat dolor ultricies. Mauris quis dui porttitor, ultrices turpis vitae,
     pulvinar nisl. Suspendisse potenti. Ut nec cursus sapien, convallis sagittis purus. 8:8 Integer mollis nisi sed fermentum
      efficitur. Suspendisse sollicitudin sapien dui, vitae tempus lacus elementum ac. Curabitur id 18:19 purus
      diam. 18:19 Donec blandit, est nec semper convallis, arcu 7.01 libero lacinia ex, eu placerat risus est non tellus."""))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
