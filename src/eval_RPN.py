"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1160948401/?envType=daily-question&envId=2024-01-30

"""

from typing import List
from icecream import ic


def is_number(s):
    return s.lstrip('-').isnumeric()


def eval_RPN(tokens: List[str]) -> int:
    while True:
        ic(tokens)
        for i in range(len(tokens) - 1):
            ic(tokens[i], tokens[i + 1], tokens[i + 2])
            if is_number(tokens[i]) and is_number(tokens[i + 1]) and not is_number(tokens[i + 2]):
                eval_str = tokens[i] + " " + tokens[i + 2] + " " + tokens[i + 1]
                tokens = tokens[:i] + [str(int(eval(eval_str)))] + tokens[i + 3:]
                ic(eval_str, tokens)
                break
        if len(tokens) == 1:
            return int(tokens[0])


if __name__ == '__main__':
    ic(eval_RPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
