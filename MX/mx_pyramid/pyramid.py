"""Program that creates beautiful pyramids."""


def make_pyramid(base: int, char: str) -> list:
    """
    Construct a pyramid with given base.

    Pyramid should consist of given chars, all empty spaces in the pyramid list are ' '. Pyramid height depends on base length. Lowest floor consists of base-number chars.
    Every floor has 2 chars less than the floor lower to it.
    make_pyramid(3, "A") ->
    [
        [' ', 'A', ' '],
        ['A', 'A', 'A']
    ]
    make_pyramid(6, 'a') ->
    [
        [' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'a', 'a', 'a', 'a', ' '],
        ['a', 'a', 'a', 'a', 'a', 'a']
    ]
    :param base: int
    :param char: str
    :return: list
    """
    if base % 2 == 0:
        counter = base // 2
    else:
        counter = base // 2 + 1
    return [build_line(i, base, char) for i in range(counter - 1, -1, -1)]


def build_line(line_num: int, base: int, char: str) -> list:
    """Build line for pyramid."""
    if base - line_num == base:
        return [char for i in range(base)]
    line = [" " for i in range(line_num)] + [char for i in range(base - 2 * line_num)] + [" " for i in range(line_num)]
    return line


def join_pyramids(pyramid_a: list, pyramid_b: list) -> list:
    """
    Join together two pyramid lists.

    Get 2 pyramid lists as inputs. Join them together horizontally. If the the pyramid heights are not equal, add empty lines on the top until they are equal.
    join_pyramids(make_pyramid(3, "A"), make_pyramid(6, 'a')) ->
    [
        [' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'A', ' ', ' ', 'a', 'a', 'a', 'a', ' '],
        ['A', 'A', 'A', 'a', 'a', 'a', 'a', 'a', 'a']
    ]

    :param pyramid_a: list
    :param pyramid_b: list
    :return: list
    """
    counter = 0
    base_a = len(pyramid_a[len(pyramid_a) - 1])
    base_b = len(pyramid_b[len(pyramid_b) - 1])
    if base_a > base_b:
        for i in range(len(pyramid_a)):
            if len(pyramid_a) - len(pyramid_b) > i:
                pyramid_a[i] += [' ' for i in range(base_b)]
            else:
                pyramid_a[i] += pyramid_b[counter]
                counter += 1
        return pyramid_a
    else:
        for i in range(len(pyramid_b)):
            if len(pyramid_b) - len(pyramid_a) > i:
                pyramid_b[i] = [' ' for i in range(base_a)] + pyramid_b[i]
            else:
                pyramid_b[i] = pyramid_a[counter] + pyramid_b[i]
                counter += 1
        return pyramid_b


def to_string(pyramid: list) -> str:
    """
    Return pyramid list as a single string.

    Join pyramid list together into a string and return it.
    to_string(make_pyramid(3, 'A')) ->
    '''
     A
    AAA
    '''

    :param pyramid: list
    :return: str
    """
    result = ""
    for line in pyramid:
        for element in line:
            result += element
        result += "\n"
    return result


if __name__ == '__main__':
    pyramid_a = make_pyramid(5, "A")
    print(pyramid_a)  # ->
    """
    [
        [' ', 'A', ' '],
        ['A', 'A', 'A']
    ]
    """

    pyramid_b = make_pyramid(8, 'a')
    print(pyramid_b)  # ->
    """
    [
        [' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'a', 'a', 'a', 'a', ' '],
        ['a', 'a', 'a', 'a', 'a', 'a']
    ]
    """

    joined = join_pyramids(pyramid_a, pyramid_b)
    print(joined)  # ->
    """
    [
        [' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'A', ' ', ' ', 'a', 'a', 'a', 'a', ' '],
        ['A', 'A', 'A', 'a', 'a', 'a', 'a', 'a', 'a']
    ]
    """

    pyramid_string = to_string(joined)
    print(pyramid_string)  # ->
    """
         aa  
     A  aaaa 
    AAAaaaaaa
    """
