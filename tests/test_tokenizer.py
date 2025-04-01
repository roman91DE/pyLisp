import pytest
from tokenizer import tokenize_to_list

@pytest.mark.parametrize("input_str,expected", [
    # Basic expressions
    ("(+ 1 2)", ["(", "+", "1", "2", ")"]),
    ("(* 3 4)", ["(", "*", "3", "4", ")"]),

    # Extra whitespace
    (" ( +   10\t  20\n) ", ["(", "+", "10", "20", ")"]),
    ("\n(+\t1   2)", ["(", "+", "1", "2", ")"]),

    # # Negative numbers and subtraction
    # ("(- -5 -10)", ["(", "-", "-5", "-10", ")"]),

    # Floats
    ("(+ 1.5 2.0)", ["(", "+", "1.5", "2.0", ")"]),
    ("(* 3.14\t2)", ["(", "*", "3.14", "2", ")"]),

    # Booleans
    ("(and true false)", ["(", "and", "true", "false", ")"]),
    ("(or\tfalse true)", ["(", "or", "false", "true", ")"]),

    # Mixed value types
    ("(= true 1)", ["(", "=", "true", "1", ")"]),
    ("(== true 1)", ["(", "==", "true", "1", ")"]),
    ("(< 2.5 10)", ["(", "<", "2.5", "10", ")"]),

    # Multiple expressions
    ("(+ 1 2) (* 3 4)", ["(", "+", "1", "2", ")", "(", "*", "3", "4", ")"]),

    # Nested expressions
    ("(+ 1 (* 2 3))", ["(", "+", "1", "(", "*", "2", "3", ")", ")"]),
    ("(define x (+ 1 2))", ["(", "define", "x", "(", "+", "1", "2", ")", ")"]),

    # Edge cases
    ("()", ["(", ")"]),
    ("( )", ["(", ")"]),
    ("", []),
    ("   ", []),
])
def test_tokenize_to_list(input_str, expected):
    assert tokenize_to_list(input_str) == expected