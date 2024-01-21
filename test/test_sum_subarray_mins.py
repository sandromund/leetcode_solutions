"""
Test for sum_subarray_mins.py
"""

from src.sum_subarray_mins import sum_subarray_mins


def test_sum_subarray_mins_case_1():
    assert sum_subarray_mins([3, 1, 2, 4]) == 17


def test_sum_subarray_mins_case_2():
    assert sum_subarray_mins([11, 81, 94, 43, 3]) == 444
