from pyLisp import evaluate_expression


def test_simple_addition(capsys):
    evaluate_expression("(+ 1 2)")
    out = capsys.readouterr().out
    assert "Expression: (1 + 2)" in out
    assert "Result: 3" in out


def test_nested_expression(capsys):
    evaluate_expression("(+ 1 (* 2 3))")
    out = capsys.readouterr().out
    assert "Expression: (1 + (2 * 3))" in out
    assert "Result: 7" in out


def test_boolean_logic(capsys):
    evaluate_expression("(& true false)")
    out = capsys.readouterr().out
    assert "Expression: (True & False)" in out
    assert "Result: False" in out


def test_comparison_lt(capsys):
    evaluate_expression("(< 1 2)")
    out = capsys.readouterr().out
    assert "Expression: (1 < 2)" in out
    assert "Result: True" in out


def test_equality(capsys):
    evaluate_expression("(== 3 3)")
    out = capsys.readouterr().out
    assert "Expression: (3 == 3)" in out
    assert "Result: True" in out


def test_ternary_true(capsys):
    evaluate_expression("(IfThenElse true 10 20)")
    out = capsys.readouterr().out
    assert "Result: 10" in out


def test_ternary_false(capsys):
    evaluate_expression("(IfThenElse false 10 20)")
    out = capsys.readouterr().out
    assert "Result: 20" in out


def test_division(capsys):
    evaluate_expression("(/ 6 2)")
    out = capsys.readouterr().out
    assert "Result: 3.0" in out


def test_division_by_zero(capsys):
    evaluate_expression("(/ 1 0)")
    out = capsys.readouterr().out
    assert "Result: None" in out


def test_unbalanced_parentheses(capsys):
    evaluate_expression("(+ 1 2")
    out = capsys.readouterr().out
    assert "Error: Unbalanced parentheses" in out


def test_unknown_operator(capsys):
    evaluate_expression("(@ 1 2)")
    out = capsys.readouterr().out
    assert "Error: Failed to parse expression." in out


def test_malformed_expression(capsys):
    evaluate_expression("(+ 1 (2 3))")
    out = capsys.readouterr().out
    assert "Error: Failed to parse expression." in out
