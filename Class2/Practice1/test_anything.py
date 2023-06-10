import anything
import pytest


def test_print_hello():
    """ Returns the Hello world """
    result = anything.print_hello()
    assert result == "Hello world"


def test_print_given(data):
    """ Returns the given data """
    result = anything.print_given(data)
    assert result == data


@pytest.mark.parametrize("number, expected",
                         [(2, 2), (13, 4), (159, 15)])
def test_sum_of_numbers(number, expected):
    result = anything.sum_of_numbers(number)
    assert result == expected
