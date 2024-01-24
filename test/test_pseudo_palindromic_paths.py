from src.pseudo_palindromic_paths import Solution, TreeNode


def test_pseudo_paths_example_1():
    """
    There are three paths going from the root node to leaf nodes:
    the path [2,3,3], the path [2,1,1], and the path [2,3,1].
    Among these paths only red path and green path are pseudo-palindromic
    paths since the  path [2,3,3] can be rearranged in [3,2,3] (palindrome)
    and the  path [2,1,1] can be rearranged in [1,2,1] (palindrome).
    :return:
    """
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
    assert sol.pseudoPalindromicPaths(head) == 2
