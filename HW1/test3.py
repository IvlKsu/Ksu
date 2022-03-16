from typing import List

nums: list[int] = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    n = 0
    sum_max = 0
    # let's calculate the sum of the first k members. And let's call it the maximum sum
    while n < k:
        sum_max += nums[n]
        n += 1
    # since the sum of the first K terms is calculated, we start further with n =1
    n = 1
    # we declare how long the cycle works
    while n <= len(nums) - k:
        try:
            t = n
            # sum_temp is a new variable that we will use in order to calculate the sum of the next subset of the long k
            sum_temp = 0
            while t < n + k:
                sum_temp += nums[t]
                t += 1
            if sum_temp > sum_max:
                sum_max = sum_temp
            n += 1
        except IndexError:
            break

    return print(sum_max)


find_maximal_subarray_sum(nums, k)
