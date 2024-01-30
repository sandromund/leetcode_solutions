"""
1074. Number of Submatrices That Sum to Target

Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are
different if they have some coordinate that is different: for example, if x1 != x1'.

https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description/?envType=daily-question&envId=2024-01-28

"""
from typing import List


def num_sub_matrix_sum_target(matrix: List[List[int]], target: int) -> int:
    """
    https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/solutions/4636406/c-java-python-javascript-2-approaches-explained/?envType=daily-question&envId=2024-01-28
    """
    m, n = len(matrix), len(matrix[0])
    for row in range(m):
        for col in range(1, n):
            matrix[row][col] += matrix[row][col - 1]
    count = 0
    for c1 in range(n):
        for c2 in range(c1, n):
            prefix_sum_count = {0: 1}
            sum_val = 0
            for row in range(m):
                sum_val += matrix[row][c2] - (matrix[row][c1 - 1] if c1 > 0 else 0)
                count += prefix_sum_count.get(sum_val - target, 0)
                prefix_sum_count[sum_val] = prefix_sum_count.get(sum_val, 0) + 1
    return count
