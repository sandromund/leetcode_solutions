from src.daily_temperatures import daily_temperatures


def test_daily_temperatures_example_1():
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_daily_temperatures_example_2():
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]


def test_daily_temperatures_example_3():
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0]
