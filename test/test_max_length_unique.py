from src.max_length_unique import Solution


def test_max_length_unique_example_1():
    """
    Input: arr = ["un","iq","ue"]
    Output: 4
    Explanation: All the valid concatenations are:
    - ""
    - "un"
    - "iq"
    - "ue"
    - "uniq" ("un" + "iq")
    - "ique" ("iq" + "ue")
    Maximum length is 4.
    """
    assert Solution().max_length_(["un", "iq", "ue"]) == 4


def test_max_length_unique_example_2():
    """
    Input: arr = ["cha","r","act","ers"]
    Output: 6
    Explanation: Possible longest valid concatenations
    are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
    """
    assert Solution().max_length_(["cha", "r", "act", "ers"]) == 6


def test_max_length_unique_example_3():
    """
    Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
    Output: 26
    Explanation: The only string in arr has all 26 characters.
    """
    assert Solution().max_length_(["abcdefghijklmnopqrstuvwxyz"]) == 26
