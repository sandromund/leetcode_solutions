"""
Test for min_falling_path_sum.py
"""
from src.min_falling_path_sum import min_falling_path_sum


def test_min_falling_path_sum_case_1():
    matrix = [[2, 1, 3],
              [6, 5, 4],
              [7, 8, 9]]
    assert min_falling_path_sum(matrix) == 13


def test_min_falling_path_sum_case_2():
    matrix = [[-19, 57],
              [-40, -5]]
    assert min_falling_path_sum(matrix) == -59


def test_min_falling_path_sum_case_3():
    matrix = [[100, -42, -46, -41],
              [31, 97, 10, -10],
              [-58, -51, 82, 89],
              [51, 81, 69, -51]]
    assert min_falling_path_sum(matrix) == -36

