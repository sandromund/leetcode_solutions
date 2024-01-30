"""
Longest Common Subsequence - Dynamic Programming - Leetcode 1143

Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some
characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

"""

from icecream import ic


def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Time and Memory in O(len_text_1 * len_text_2)

    https://www.youtube.com/watch?v=Ua0GhsJSlWM


    """
    len_text_1 = len(text1)
    len_text_2 = len(text2)
    dp = [[0] * (len_text_2 + 1)
          for _ in range((len_text_1 + 1))]

    for i in range(len_text_1 - 1, -1, -1):
        for j in range(len_text_2 - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
            ic(dp, i, j, text1[i], text2[j])

    return dp[0][0]


if __name__ == '__main__':
    ic(longest_common_subsequence(text1="abcde", text2="ace"))
