"""
Given a binary tree where node values are digits from 1 to 9.
A path in the binary tree is said to be pseudo-palindromic if at
least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

"""
from collections import Counter
from icecream import ic


class TreeNode(object):
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    """
    https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/
    ?envType=daily-question&envId=2024-01-24
    """

    def __init__(self):
        self.result = 0

    @staticmethod
    def is_pseudo_palindromic(path: str) -> bool:
        c = Counter(path)
        r = sum([k % 2 for k in c.values()])
        ic(path, r, c)
        if r == 0 or r == 1:
            return True
        return False

    def recursive(self, root: TreeNode, path: str):
        """
        Memory Limit Exceeded
        """
        path += str(root.val)
        if root.left is None and root.right is None:
            if self.is_pseudo_palindromic(path):
                self.result += 1
        else:
            if root.left is not None:
                self.recursive(root.left, path)
            if root.right is not None:
                self.recursive(root.right, path)

    def dfs_xor(self, root):
        """
        Needed help

       https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/solutions/
       4616403/beats-99-02-users-c-java-python-javascript-2-approaches-explained/
       ?envType=daily-question&envId=2024-01-24
        """
        count = 0
        stack = [(root, 0)]
        while stack:
            node, path = stack.pop()
            if node:
                path_before = path
                path ^= 1 << node.val
                ic(path_before, node.val, 1 << node.val, path)
                if not node.left and not node.right:
                    if path & (path - 1) == 0:
                        ic(path, path & (path - 1))
                        count += 1
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))

        return count

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        # self.recursive(root, "")
        # return self.result
        return self.dfs_xor(root)


if __name__ == '__main__':

    ic(1, 1 << 1, 1 << 2, 1 << 3)
    ic(1 ^ 1, 2 ^ 1, 2 ^ 2)

    sol = Solution()

    head = TreeNode(
        val=2,
        left=TreeNode(
            val=3,
            left=TreeNode(val=3),
            right=TreeNode(val=1)),
        right=TreeNode(
            val=1,
            right=TreeNode(val=1)))

    ic(sol.pseudoPalindromicPaths(head))
