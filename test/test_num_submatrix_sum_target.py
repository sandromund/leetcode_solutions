from src.num_submatrix_sum_target import num_sub_matrix_sum_target


def test_num_sub_matrix_sum_target_example_1():
    """
    Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
    Output: 4
    Explanation: The four 1x1 submatrices that only contain 0.
    """
    assert num_sub_matrix_sum_target(matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0) == 4


def test_num_sub_matrix_sum_target_example_2():
    """
    Input: matrix = [[1,-1],[-1,1]], target = 0
    Output: 5
    Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
    """
    assert num_sub_matrix_sum_target(matrix=[[1, -1], [-1, 1]], target=0) == 5


def test_num_sub_matrix_sum_target_example_3():
    """
    Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
    Output: 4
    Explanation: The four 1x1 submatrices that only contain 0.
    """
    assert num_sub_matrix_sum_target(matrix=[[904]], target=0) == 0
