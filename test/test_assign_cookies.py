from src.assign_cookies import Solution


def test_assign_cookies_example_1():
    """
    Input: g = [1,2,3], s = [1,1]
    Output: 1
    Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
    And even though you have 2 cookies, since their size is both 1,
    you could only make the child whose greed factor is 1 content.
    You need to output 1.
    """
    assert Solution().find_content_children(g=[1, 2, 3], s=[1, 1]) == 1


def test_assign_cookies_example_2():
    """
    Input: g = [1,2], s = [1,2,3]
    Output: 2
    Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
    You have 3 cookies and their sizes are big enough to gratify all of the children,
    You need to output 2.
    """
    assert Solution().find_content_children(g=[1, 2], s=[1, 2, 3]) == 2


def test_assign_cookies_case_2():
    assert Solution().find_content_children(g=[1, 2, 3], s=[]) == 0


def test_assign_cookies_case_10():
    assert Solution().find_content_children(g=[10, 9, 8, 7], s=[5, 6, 7, 8]) == 2
