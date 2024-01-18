"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
"""


def climb_stairs(n: int) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if n == 1:
        return 1
    arr = [0] * (n + 1)
    cnt = 3
    arr[1] = 1
    arr[2] = 2
    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
        cnt += 1
    return arr[cnt - 1]
