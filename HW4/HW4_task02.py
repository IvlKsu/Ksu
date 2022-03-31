"""
Write a function that gets file path as an argument.
Read the first line of the file.
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.

Write a test for that function using pytest library.

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - all temporary files are removed after test run

You will learn:
 - how to test Exceptional cases
 - how to clean up after tests
 - how to check if file exists**
 - how to handle*** and raise**** exceptions in test. Use sample from the documentation.

* https://en.wikipedia.org/wiki/Interval_(mathematics)#Terminology
** https://docs.python.org/3/library/os.path.html
*** https://docs.python.org/3/tutorial/errors.html#handling-exceptions
**** https://docs.python.org/3/tutorial/errors.html#raising-exceptions
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

#print(read_magic_number("1.txt"))