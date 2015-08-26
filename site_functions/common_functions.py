__author__ = 'boomatang'
__version__ = '1'


def string_shorten(text, max_length=115):
    """
    Function that shortens the length of a string and adds "..." on to the end.

    :param text: String in put for the length to be check and/or reformatted
    :param max_length: The value of allowed length of the String. Defaults to 115.
    """
    if len(text) > max_length:
        new_text = text[:max_length] + "..."

    else:
        new_text = text

    return new_text
