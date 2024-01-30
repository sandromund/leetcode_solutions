from src.eval_RPN import eval_RPN


def test_eval_RPN_example_1():
    """
    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9
    """
    assert eval_RPN(["2", "1", "+", "3", "*"]) == 9


def test_eval_RPN_example_2():
    """
    Input: tokens = ["4","13","5","/","+"]
    Output: 6
    Explanation: (4 + (13 / 5)) = 6
    """
    assert eval_RPN(["4", "13", "5", "/", "+"]) == 6


def test_eval_RPN_example_3():
    """
    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22
    Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22
    """
    assert eval_RPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
