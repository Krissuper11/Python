"""Caesar cipher"""


def encode(message: str, shift: int) -> str:
    """Encode a message using a Caesar cipher."""
    new_letter = ""
    for i in range(len(message)):
        if message[i] == " ":
            new_letter += " "
        else:
            index = ord(message[i]) + shift
            index -= 26 * ((index - 97) // 26)
            new_letter += chr(index)
    return new_letter
