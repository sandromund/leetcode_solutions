"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses
have security systems connected, and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

"""
from typing import List

from icecream import ic


def rob(nums: List[int]) -> int:
    """
    Time complexity:    O(n)
    Space complexity:   O(n)

    Solved it fast without any help. :)

    Runtime Beats 86.54% of users with Python3
    Memory Beats 56.96% of users with Python3
    """
    n = len(nums)
    if n == 0:
        return 0
    if n < 3:
        return max(nums)
    dya = [0] * n
    dya[0] = nums[0]
    dya[1] = nums[1]
    for i in range(2, n):
        dya[i] = nums[i] + max(dya[i - 2], dya[i - 3])
    return max(dya[n - 1], dya[n - 2])


if __name__ == '__main__':
    ic(rob([2, 1, 1, 2]))
