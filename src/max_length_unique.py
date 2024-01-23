"""
1239. Maximum Length of a Concatenated String with Unique Characters

You are given an array of strings arr. A string s is formed by the concatenation of a subsequence
of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting
some or no elements without changing the order of the remaining elements.

"""
from typing import List
from icecream import ic


class Solution:

    def __init__(self):
        self.max_length = 0
        self.n = None
        self.arr = None

    @staticmethod
    def is_unique(s: str) -> bool:
        return len(s) == len(set(s))

    def backtrack(self, index: int, current: str) -> None:
        self.max_length = max(self.max_length, len(current))
        ic(index, current, self.max_length)
        for i in range(index, self.n):
            if self.is_unique(current + self.arr[i]):
                self.backtrack(i + 1, current + self.arr[i])

    def max_length_(self, arr: List[str]) -> int:
        self.n = len(arr)
        self.arr = arr
        self.backtrack(0, "")
        return self.max_length


if __name__ == '__main__':
    sol = Solution()
    ic(sol.max_length_(["cha", "r", "act", "ers"]))
