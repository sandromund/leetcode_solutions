from src.find_judge import find_judge


def test_find_judge_example_1():
    assert find_judge(n=2, trust=[[1, 2]]) == 2


def test_find_judge_example_2():
    assert find_judge(n=3, trust=[[1, 3], [2, 3]]) == 3


def test_find_judge_example_3():
    assert find_judge(n=3, trust=[[1, 3], [2, 3], [3, 1]]) == -1


def test_find_judge_test_7():
    assert find_judge(n=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3


def test_find_judge_test_87():
    assert find_judge(n=3, trust=[[1, 2], [2, 3]]) == -1
