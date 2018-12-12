"""To test multi-bracket_validation function."""
# from data_structures_and_algorithms. import multi_bracket_validation
from .. multi_bracket_validation import multi_bracket_validation


def test_function_exist():
    """To test function exists."""
    assert multi_bracket_validation


def test_to_be_true_1():
    """To test function returns true - 1."""
    str_ = '{}'
    assert multi_bracket_validation(str_) is True


def test_to_be_true_2():
    """To test function returns true - 2."""
    str_ = '{}(){}'
    assert multi_bracket_validation(str_) is True


def test_to_be_true_3():
    """To test function returns true - 3."""
    str_ = '()[[Extra Characters]]'
    assert multi_bracket_validation(str_) is True


def test_to_be_true_4():
    """To test function returns true - 4."""
    str_ = '(){}[[]]'
    assert multi_bracket_validation(str_) is True


def test_to_be_true_5():
    """To test function returns true - 5."""
    str_ = '{}{Code}[Fellows](())'
    assert multi_bracket_validation(str_) is True


def test_to_be_false_1():
    """To test function returns false - 1."""
    str_ = '[({}]'
    assert multi_bracket_validation(str_) is False


def test_to_be_false_2():
    """To test function returns false - 2."""
    str_ = '(]('
    assert multi_bracket_validation(str_) is False


def test_to_be_false_3():
    """To test function returns false - 3."""
    str_ = '{(})'
    assert multi_bracket_validation(str_) is False
