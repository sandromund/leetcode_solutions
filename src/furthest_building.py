"""
1642. Furthest Building You Can Reach

https://leetcode.com/problems/furthest-building-you-can-reach/description/?envType=daily-question&envId=2024-02-17

You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.


Old Time Limit Exceeded in this solution:

    def get_diffs(heights: List[int]):
        n = len(heights)
        diffs = []
        indices = [-1]
        diffs_i = -1
        for i in range(n - 1):
            k = heights[i + 1] - heights[i]
            if k > 0:
                diffs.append(k)
                diffs_i += 1
            indices.append(diffs_i)
        return diffs, indices

    def furthest_building_slow(heights: List[int], bricks: int, ladders: int) -> int:

        diffs, index_list = get_diffs(heights)

        ladder_bricks = []  # indices of the biggest diffs we can replace with ladders
        sei = None  # smallest_element_index
        diff_sum = 0

        goal_i = -1
        for i, diff in enumerate(diffs):
            diff_sum += diff
            if ladders > 0:
                if len(ladder_bricks) < ladders:
                    ladder_bricks.append(diff)
                    if sei is None:
                        sei = 0
                    elif ladder_bricks[sei] > diff:
                        sei = len(ladder_bricks) - 1
                elif ladder_bricks[sei] < diff:
                    ladder_bricks[sei] = diff
                    sei = ladder_bricks.index(min(ladder_bricks))

            if not (bricks + sum(ladder_bricks) >= diff_sum):
                break
            goal_i += 1
        result = len(index_list) - 1 - index_list[::-1].index(goal_i)

        return result
"""

import heapq
from itertools import pairwise
from typing import List


# https://leetcode.com/problems/furthest-building-you-can-reach/solutions/4739370/straightforward-python-solution/?envType=daily-question&envId=2024-02-17
def furthest_building(heights: List[int], bricks: int, ladders: int) -> int:
    jumps = []
    for i, (h0, h1) in enumerate(pairwise(heights)):
        if (d := h1 - h0) > 0:
            heapq.heappush(jumps, d)
        if len(jumps) > ladders:
            bricks -= heapq.heappop(jumps)
        if bricks < 0:
            return i
    return len(heights) - 1
