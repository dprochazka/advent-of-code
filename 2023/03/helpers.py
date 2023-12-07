def is_digit(char):
    return char in "1234567890"


def is_symbol(char):
    return char != "." and not is_digit(char)
