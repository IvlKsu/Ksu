import HW2.hw2_task01 as task1

import random


N = 3
range_of_values = 10
A = []
B = []
C = []
for i in range(0, N):
    A.append(random.randint(-range_of_values, range_of_values))
    B.append(random.randint(-range_of_values, range_of_values))
    C.append(random.randint(-range_of_values, range_of_values))


def test_task1():
    result = task1.combinations(A, B, C)
    assert result != None
    assert len(result) > 0
    assert type(result) == list
    assert task1.combinations([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
