"""Caesar cipher."""


def encode(message: str, shift: int) -> str:
    """Encode a message using a Caesar cipher."""
    new_letter = ""
    for i in range(len(message)):
        if not message[i].isalpha():
            new_letter += message[i]
        elif message[i].isalpha():
            index = ord(message[i]) + shift
            index -= 26 * ((index - 97) // 26)
            new_letter += chr(index)
        else:
            pass
    return new_letter
print(encode("ab c ' _+", 3))