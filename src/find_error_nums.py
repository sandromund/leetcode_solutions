"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately,
due to some error, one of the numbers in s got duplicated to another number in the set, which results
in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""

from typing import List
from icecream import ic


def find_error_nums(nums: List[int]) -> List[int]:
    """
    Time complexity: O(n * log(n) because of sorting
    Space complexity: O(1)


    156 ms Beats 86.38% of users with Python
    17.81 MB Beats 89.31% of users with Python

    """
    duplicated = None
    missing = None
    nums = sorted(nums)
    if nums[0] != 1:
        missing = 1
    n = len(nums)
    for i in range(n):
        last = nums[i - 1]
        current = nums[i]
        if last + 1 == current:
            continue
        if last < current:
            missing = last + 1
            if duplicated is not None:
                return [duplicated, missing]
        elif last == current:
            duplicated = current
            if missing is not None:
                return [duplicated, missing]
    return [duplicated, n]


if __name__ == '__main__':
    a = [1, 5, 3, 2, 2, 7, 6, 4, 8, 9]
    ic(sorted(a))
    ic(find_error_nums(a))
