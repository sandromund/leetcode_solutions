from src.longest_common_subsequence import longest_common_subsequence


def test_longest_common_subsequence_example_1():
    assert longest_common_subsequence(text1="abcde", text2="ace") == 3
