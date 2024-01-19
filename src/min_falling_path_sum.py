"""
Given an n x n array of integers matrix,
return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in
the next row that is either directly below or diagonally left/right.
Specifically, the next element from position (row, col) will be (row + 1, col - 1),
(row + 1, col), or (row + 1, col + 1).

"""
from icecream import ic


def min_falling_path_sum(matrix: list[list[int]]) -> int:
    """
    Time complexity: O(n) the number of cells in the matrix
    Space complexity: O(n) < number of cells * 3

    109 ms Beats 40.22% of users with Python
    12.54 MB Beats 100.00% of users with Python
    """
    n = len(matrix)
    steps = [[0] * n] * n
    steps[0] = matrix[0]
    for i in range(1, n):
        step = []
        for j in range(n):
            candidates = [steps[i - 1][j]]
            if j - 1 >= 0:
                candidates.append(steps[i - 1][j - 1])
            if j + 1 < n:
                candidates.append(steps[i - 1][j + 1])
            step.append(matrix[i][j] + min(candidates))
        steps[i] = step
    return min(steps[n - 1])


if __name__ == '__main__':
    m = [[100, -42, -46, -41],
         [31, 97, 10, -10],
         [-58, -51, 82, 89],
         [51, 81, 69, -51]]
    ic(min_falling_path_sum(m))
