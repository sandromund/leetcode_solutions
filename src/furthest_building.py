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


def get_diffs(heights: List[int]):
    """
    ic| heights:    [ 4, 2, 7, 6, 9, 14, 12]
    ic| index_list: [-1,-1, 0, 0, 1, 2,  2]
    ic| diffs: [5, 3, 5]

    """
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


def get_diff_sums(diffs):
    r = []
    k = 0
    for d in diffs:
        k += d
        r.append(k)
    return r


def furthest_building(heights: List[int], bricks: int, ladders: int) -> int:
    diffs, index_list = get_diffs(heights)

    ladder_bricks = []  # indices of the biggest diffs we can replace with ladders
    sei = None  # smallest_element_index
    diff_sums = get_diff_sums(diffs)

    goal_i = -1
    for i, diff in enumerate(diffs):
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

        ic(goal_i, ladder_bricks, diff_sums[i], sum(ladder_bricks), bricks)

        if not (bricks + sum(ladder_bricks) >= diff_sums[i]):
            break
        goal_i += 1

    result = len(index_list) - 1 - index_list[::-1].index(goal_i)

    ic(heights)
    ic(index_list)
    ic(diffs)
    ic(diff_sums)
    ic(result)
    return result


if __name__ == '__main__':
    furthest_building(heights=[14, 3, 19, 3], bricks=17, ladders=0)
