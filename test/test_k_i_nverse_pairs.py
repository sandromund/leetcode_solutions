from src.k_i_nverse_pairs import k_inverse_pairs


def test_k_inverse_pairs_example_1():
    """
    Input: n = 3, k = 0
    Output: 1
    Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
    """
    assert k_inverse_pairs(n=3, k=0) == 1


def test_k_inverse_pairs_example_2():
    """
    Input: n = 3, k = 1
    Output: 2
    Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
    """
    assert k_inverse_pairs(n=3, k=1) == 2


