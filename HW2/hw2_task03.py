"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Any


def new_character_string(mas: str, *args: Any):
    if len(args) == 1: # if only one argument is passed, then
        #assigns the index variable the index value of the first occurrence of this argument in the string
        index = mas.index(args[0])
        #we return a string with values up to the entered argument
        return mas[:index]
    elif len(args) == 2:
        """
        if we have 2 arguments, then we denote the length of our tuple . To do this, we denote the 
        initial index (index of occurrence of 1 argument) and the final index (index of occurrence of 2 arguments).
         And we will return the resulting sequence.
        """
        start_index = mas.index(args[0])
        end_index = mas.index(args[1])
        return mas[start_index:end_index]
    elif len(args) == 3:
        """
        if we have 3 arguments, then we denote the length of our tuple . To do this, we denote the 
        initial index (index of occurrence of 1 argument) and the final index (index of occurrence of 2 arguments).
        And we will return the sequence from the first to the last , taking into account 3 arguments
        """
        start_index = mas.index(args[0])
        end_index = mas.index(args[1])
        return mas[start_index:end_index:args[2]]
    else:
        return mas

print(new_character_string("abcdefg", "b", "f" ))
print(new_character_string("abcdefg", "f", "a", -2))


