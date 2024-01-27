"""
629. K Inverse Pairs Array

For an integer array nums, an inverse pair is a pair of
integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays
consist of numbers from 1 to n such that there are exactly
k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.


"""
from icecream import ic

"""
https://leetcode.com/problems/k-inverse-pairs-array/solutions/4633266/dp-python-easy/?envType=daily-question&envId=2024-01-27
"""

def k_inverse_pairs(n: int, k: int) -> int:
    MOD = 10 ** 9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        prefix_sum = 0
        for j in range(k + 1):
            prefix_sum = (prefix_sum + dp[i - 1][j]) % MOD
            if j >= i:
                prefix_sum = (prefix_sum - dp[i - 1][j - i] + MOD) % MOD
            dp[i][j] = prefix_sum
        ic(i, dp)

    return dp[n][k]


if __name__ == '__main__':
    ic(k_inverse_pairs(n=5, k=3))
