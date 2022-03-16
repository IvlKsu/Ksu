from typing import List

#create four lists and pass the value
A: list[int] = [1, 2, 3]
B: list[int] = [-5, -1, 2]
C: list[int] = [0, -1, -3]
D: list[int] = [4, 0, 1]


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    # the number of tuples that are zero
    counter = 0
    #let's list the values from the array
    for i in a:
        for j in b:
            for k in c:
                for l in d:
                    sum = i + j + k + l   #A[i]+B[j]+C[k]+D[l]
                    if sum == 0:
                        counter += 1

    return print(counter)


check_sum_of_four(A, B, C, D)
