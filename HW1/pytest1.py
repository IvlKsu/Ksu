from HW1.test2 import check_sum_of_four


def test_task1():
    assert check_sum_of_four([1, 2, 3], [-5, -1, 2], [0, -1, -3], [4, 0, 1]) == 7
