from HW5.HW6_task02 import custom_sum
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(1, 2, 3), ([1, 2], [3, 4], [1, 2, 3, 4])])
def test_custom_sum(a, b, expected_result):
    assert custom_sum(a, b) == expected_result


def test_custom_sum_name_attribute():
    assert custom_sum.__name__ == 'custom_sum'


def test_custom_sum_doc_attribute():
    assert custom_sum.__doc__ == 'This function can sum any objects which have __add___'


def test_custom_sum_orig_func():
    assert str(custom_sum.__original_func)[:23] == '<function custom_sum at'
