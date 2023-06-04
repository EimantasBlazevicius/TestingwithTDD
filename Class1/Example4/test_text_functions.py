import text_functions


def test_swap_case(text):
    assert text_functions.swap_case(text) == "QWE qwe ASD i"


def test_shortest_word(text):
    assert text_functions.shortest_word(text) == "I"

