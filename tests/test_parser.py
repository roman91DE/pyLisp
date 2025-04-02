import pytest

from expression import LT, Addition, Boolean, Empty, IfThenElse
from parser import bracket_check, parse_tokens
from tokenizer import tokenize_to_list


def test_addition() -> None:
    tokens = tokenize_to_list("(+ 1 2)")
    assert bracket_check(tokens)
    expr = parse_tokens(tokens)
    assert isinstance(expr, Addition)
    assert expr.eval() == 3


def test_comparison() -> None:
    tokens = tokenize_to_list("(< 2 5)")
    assert bracket_check(tokens)
    expr = parse_tokens(tokens)
    assert isinstance(expr, LT)
    assert expr.eval() == Boolean(True)


def test_empty() -> None:
    tokens = tokenize_to_list("()")
    assert bracket_check(tokens)
    expr = parse_tokens(tokens)
    assert isinstance(expr, Empty)
    assert expr.eval() is None


def test_if_then_else() -> None:
    tokens = tokenize_to_list("(IfThenElse (< 2 3) 100 200)")
    assert bracket_check(tokens)
    expr = parse_tokens(tokens)
    assert isinstance(expr, IfThenElse)
    assert expr.eval() == 100


@pytest.mark.parametrize(
    "expr",
    [
        "(+ 1)",  # Wrong arity
        "(foobar 1 2)",  # Unknown symbol
        "(+ 1 (2 3))",  # Malformed
        "(+ 1 2",  # Unbalanced
    ],
)
def test_invalid_expressions(expr):
    tokens = tokenize_to_list(expr)
    if not bracket_check(tokens):
        assert True  # Correctly fails bracket check
    else:
        parsed = parse_tokens(tokens)
        assert parsed is None
