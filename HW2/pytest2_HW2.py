import HW2.hw2_task02 as task2

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


def test_task2():
    result = task2.cache_func(A[0], B[1])
    assert result != None
    assert type(result) != str
    assert (3 ** 2) ** 2 == 81