"""
Write a function that gets file path as an argument.
Read the first line of the file.
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.


>>> read_magic_number("Error_file.txt")
'Error!!!'

>>> read_magic_number("True_file.txt")
True

>>> read_magic_number("False_file.txt")
False

"""


def read_magic_number(path: str) -> bool:
    """
    This  function checks whether the file meets the conditions.
    And gives an error if the string is not a number
    """
    with open(path) as f:
        try:
            number_str = f.readline().split()
            for i in range(0, len(number_str)):
                if float(number_str[i]) >= 1. and float(number_str[i]) < 3.:
                    return True
                else:
                    return False
        except ValueError:
            print("Error!!!")


