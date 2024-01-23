"""
455. Assign Cookies

Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with;
and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i,
and the child i will be content.
Your goal is to maximize the number of your content children and output the maximum number.

"""
from typing import List
from icecream import ic


class Solution:

    """
    Submission:
    https://leetcode.com/problems/assign-cookies/submissions/1154407841?envType=daily-question&envId=2024-01-01

    """

    @staticmethod
    def find_content_children(g: List[int], s: List[int]) -> int:
        """
        Time complexity: O(n * log(n)) because of sorting
        Space complexity: O(1)

        Runtime 128 ms Beats 94.94% of users with Python3
        Memory  18.46MB Beats 96.72% of users with Python3
        """
        result = 0
        g = sorted(g)
        s = sorted(s)
        len_g = len(g)  # number of children
        len_s = len(s)  # number of cookies
        i_g = 0
        i_s = 0
        while i_s < len_s and i_g < len_g:
            if g[i_g] <= s[i_s]:
                result += 1
                i_g += 1
            i_s += 1
        return result


if __name__ == '__main__':
    ic(Solution().find_content_children(g=[10, 9, 8, 7], s=[5, 6, 7, 8]))
