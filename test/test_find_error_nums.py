from src.find_error_nums import find_error_nums


def test_find_error_nums_example_1():
    assert find_error_nums([1, 2, 2, 4]) == [2, 3]


def test_find_error_nums_example_2():
    assert find_error_nums([1, 1]) == [1, 2]


def test_find_error_nums_case_18():
    assert find_error_nums([3, 2, 3, 4, 6, 5]) == [3, 1]


def test_find_error_nums_case_19():
    assert find_error_nums([1, 5, 3, 2, 2, 7, 6, 4, 8, 9]) == [2, 10]
