import string

import HW2.hw2_task03 as task3

import random


text = string.ascii_lowercase
index_start = random.randint(0, len(text)-1)
index_end = random.randint(0, len(text)-1)
step = random.randint(1, len(text))


def test_task3():
    result = task3.new_character_string(text, text[index_start], text[index_end], step)
    assert result != None
    assert type(result) == str
    assert task3.new_character_string("abcdefg", "f", "a", -2 ) == "fdb"