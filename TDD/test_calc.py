from calc import add_numbers, divide_numbers


def test_add_numbers():
    a = 4
    b = 7
    expected = 11

    assert add_numbers(a, b) == expected


def test_divide_numbers():
    a = 100
    b = 50
    expected = 2

    assert divide_numbers(a, b) == expected
