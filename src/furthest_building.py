"""
1642. Furthest Building You Can Reach

https://leetcode.com/problems/furthest-building-you-can-reach/description/?envType=daily-question&envId=2024-02-17

You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.


"""

from typing import List

from icecream import ic


def furthest_building(heights: List[int], bricks: int, ladders: int) -> int:
    bricks_required = 0
    n = len(heights)
    diffs = []
    index_list = [0] * n
    index_index = -1
    for i in range(1, n - 1):
        k = heights[i + 1] - heights[i]
        if k > 0:
            diffs.append(k)
            index_index += 1
        index_list[i] = index_index
    ic(index_list)
    ic(diffs)
    return -1
