from src.house_robber import rob


def test_rob_example_1():
    """
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.
    """
    assert rob([1, 2, 3, 1]) == 4


def test_rob_example_2():
    """
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.
    """
    assert rob([2, 7, 9, 3, 1]) == 12


def test_rob_case_40():
    assert rob([2, 1, 1, 2]) == 4
