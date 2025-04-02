from expression import (
    AND,
    EQ,
    LT,
    NOT,
    OR,
    Addition,
    Boolean,
    Constant,
    Division,
    Empty,
    Expression,
    IfThenElse,
    Multiplication,
    Scalar,
    Subtraction,
)


def test_constant_and_boolean_eval():
    assert Constant(5).eval() == 5
    assert Constant(3.14).eval() == 3.14
    assert Boolean(True).eval() is True
    assert Boolean(False).eval() is False


def test_scalar_str_and_repr():
    assert str(Constant(42)) == "42"
    assert repr(Boolean(True)) == "True"


def test_addition_eval():
    expr = Addition(Constant(2), Constant(3))
    assert expr.eval() == 5


def test_subtraction_eval():
    expr = Subtraction(Constant(10), Constant(4))
    assert expr.eval() == 6


def test_multiplication_eval():
    expr = Multiplication(Constant(3), Constant(7))
    assert expr.eval() == 21


def test_division_eval():
    expr = Division(Constant(20), Constant(5))
    assert expr.eval() == 4


def test_division_by_zero():
    expr = Division(Constant(20), Constant(0))
    assert expr.eval() is None


def test_lt_eval():
    assert LT(Constant(3), Constant(4)).eval() == Boolean(True)
    assert LT(Constant(5), Constant(5)).eval() == Boolean(False)


def test_eq_eval():
    assert EQ(Constant(7), Constant(7)).eval() == Boolean(True)
    assert EQ(Constant(7), Constant(8)).eval() == Boolean(False)


def test_and_eval():
    assert AND(Boolean(True), Boolean(True)).eval() == Boolean(True)
    assert AND(Boolean(True), Boolean(False)).eval() == Boolean(False)


def test_or_eval():
    assert OR(Boolean(True), Boolean(False)).eval() == Boolean(True)
    assert OR(Boolean(False), Boolean(False)).eval() == Boolean(False)


def test_not_eval():
    assert NOT(Boolean(True)).eval() == Boolean(False)
    assert NOT(Boolean(False)).eval() == Boolean(True)


def test_if_then_else_true_branch():
    expr = IfThenElse(Boolean(True), Constant(10), Constant(20))
    assert expr.eval() == 10


def test_if_then_else_false_branch():
    expr = IfThenElse(Boolean(False), Constant(10), Constant(20))
    assert expr.eval() == 20


def test_nested_expression():
    expr = IfThenElse(
        LT(Addition(Constant(1), Constant(1)), Constant(3)),  # 2 < 3
        Division(Multiplication(Constant(2), Constant(5)), Constant(2)),  # 10 / 2
        Constant(0),
    )
    assert expr.eval() == 5


def test_empty_repr_and_eval():
    e = Empty()
    assert str(e) == "()"
    assert e.eval() is None


def test_boolean_isinstance_and_subclass():
    b = Boolean(True)
    assert isinstance(b, Scalar)
    assert isinstance(b, Expression)


def test_binary_operator_str_repr():
    expr = Addition(Constant(1), Constant(2))
    assert str(expr) == "(1 + 2)"
    assert repr(expr) == "+ 1 2"


def test_ternary_str_repr():
    expr = IfThenElse(Boolean(True), Constant(10), Constant(20))
    assert str(expr) == "(IF True THEN 10 ELSE 20)"
    assert repr(expr) == "(IfThenElse True 10 20)"


def test_deeply_nested_if_then_else():
    expr = IfThenElse(
        Boolean(False), Constant(0), IfThenElse(Boolean(True), Constant(1), Constant(2))
    )
    assert expr.eval() == 1


def test_eval_idempotence():
    expr = Addition(Constant(2), Constant(3))
    result = expr.eval()
    assert result == expr.eval()


def test_mixed_numeric_types():
    expr = Addition(Constant(2), Constant(3.5))
    assert expr.eval() == 5.5
    assert isinstance(expr.eval(), float)


def test_eq_return_type():
    expr = EQ(Constant(10), Constant(10))
    result = expr.eval()
    assert isinstance(result, Boolean)
    assert result == Boolean(True)


def test_float_division():
    expr = Division(Constant(9), Constant(2))
    assert expr.eval() == 4.5
