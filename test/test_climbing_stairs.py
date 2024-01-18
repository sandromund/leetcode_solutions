"""
Test of climb_stairs function
"""
from src.climbing_stairs import climb_stairs


def test_climbing_stairs_n_2():
    assert climb_stairs(2) == 2


def test_climbing_stairs_n_3():
    assert climb_stairs(3) == 3
