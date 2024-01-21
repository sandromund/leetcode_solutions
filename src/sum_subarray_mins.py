"""
Sum of Subarray Minimums

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr.
Since the answer may be large, return the answer modulo 109 + 7.
"""
from typing import List

from icecream import ic


def sum_subarray_mins_naiv(arr: List[int]) -> int:
    """
    Time Limit Exceeded
    """
    mod = 10 ** 9 + 7
    n = len(arr)
    result = 0
    for i in range(n):
        for j in range(1, n + 1):
            s = arr[i:j]
            ic(s)
            if len(s) == 0:
                continue
            k = min(s)
            result += k
            ic(k, result)
    result = result % mod
    ic(result)
    return result


def sum_subarray_mins(arr: List[int]) -> int:
    """
    Time complexity:    O(n)
    Space complexity:   O(n)
    """
    result = 0
    stack = []
    for value_i in arr:
        if not stack:
            stack.append([value_i, 1, 0])
        else:
            count = 0
            while stack and stack[-1][0] > value_i:
                n_occurrence, n_replaces, value = stack.pop()
                result += (n_occurrence * (count + n_replaces)) + (count * value * n_occurrence)
                count += n_replaces
            stack.append([value_i, 1 + count, count])
    count = 0
    while stack:
        n_occurrence, n_replaces, value = stack.pop()
        result += (n_occurrence * (count + n_replaces)) + (count * value * n_occurrence)
        count += n_replaces
    m = (10 ** 9) + 7
    return result % m


if __name__ == '__main__':
    """
    Input: arr = [3,1,2,4]
    Output: 17
    Explanation:
        Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
        Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
        Sum is 17.
    """
    ic(sum_subarray_mins([3, 1, 2, 4]))
