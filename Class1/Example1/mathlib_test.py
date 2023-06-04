import mathlib


def test_addition_result():
    """Addition returns correct value"""
    assert mathlib.addition(2, 3) == 5
    assert mathlib.addition(-5, 3) == -2


def test_addition_result_type():
    """Addition returns correct value type"""
    assert type(mathlib.addition(1, 2)) == type(9)


def test_multiply_result():
    """Multiply returns correct value"""
    assert mathlib.multiply(2, 3) == 6
    assert mathlib.multiply(2, -3) == -6


def test_multiply_result_type():
    """Multiply returns correct value type"""
    assert type(mathlib.multiply(1, 2)) == type(9)
