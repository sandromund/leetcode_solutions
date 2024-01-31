"""
739. Daily Temperatures


Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature. If there is no future
day for which this is possible, keep answer[i] == 0 instead.
"""
from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    solution = [0] * n
    stack = []
    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            index = stack.pop()
            solution[index] = i - index
        stack.append(i)
    return solution
