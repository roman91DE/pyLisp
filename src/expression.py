#!/usr/bin/env python

# In[12]:


from abc import ABC, abstractmethod
from dataclasses import dataclass
from numbers import Number
from sys import stderr
from typing import Generic, LiteralString, TypeVar

# In[13]:


class Expression(ABC):
    @abstractmethod
    def eval(self) -> Number:
        pass


class Empty(Expression):
    def eval(self) -> None:
        return None

    def __repr__(self) -> LiteralString:
        return "()"

    def __str__(self) -> LiteralString:
        return self.__repr__()


# In[ ]:


T = TypeVar("T", bound=object)


@dataclass(repr=False, eq=True, frozen=True)
class Scalar(Expression, Generic[T]):
    value: T

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self)

    def eval(self) -> T:
        return self.value


class Boolean(Scalar[bool]):
    pass


class Constant(Scalar[int | float]):
    pass


# In[15]:
class UnaryOperator(Expression):
    def __init__(self, val: Expression) -> None:
        self.lhs = val

    @abstractmethod
    def operator_symbol() -> str:
        pass

    def __repr__(self) -> str:
        return f"{self.operator_symbol()} {self.lhs}"

    def __str__(self) -> str:  # called for print
        return f"({self.operator_symbol()} {self.lhs})"


class NOT(UnaryOperator):
    @staticmethod
    def operator_symbol() -> LiteralString:
        return "!"

    def eval(self) -> Boolean:
        return Boolean(not bool(self.lhs.eval()))


class BinaryOperator(Expression):
    def __init__(self, lhs: Expression, rhs: Expression) -> None:
        self.lhs = lhs
        self.rhs = rhs

    @abstractmethod
    def operator_symbol() -> str:
        pass

    def __repr__(self) -> str:
        return f"{self.operator_symbol()} {self.lhs} {self.rhs}"

    def __str__(self) -> str:  # called for print
        return f"({self.lhs} {self.operator_symbol()} {self.rhs})"


class Addition(BinaryOperator):
    @staticmethod
    def operator_symbol() -> LiteralString:
        return "+"

    def eval(self) -> Number:
        return self.lhs.eval() + self.rhs.eval()


class Subtraction(BinaryOperator):
    @staticmethod
    def operator_symbol() -> LiteralString:
        return "-"

    def eval(self) -> Number:
        return self.lhs.eval() - self.rhs.eval()


class Multiplication(BinaryOperator):
    @staticmethod
    def operator_symbol() -> LiteralString:
        return "*"

    def eval(self) -> Number:
        return self.lhs.eval() * self.rhs.eval()


class Division(BinaryOperator):
    @staticmethod
    def operator_symbol() -> LiteralString:
        return "/"

    def eval(self) -> Number | None:
        denominator = self.rhs.eval()
        if denominator == 0:
            print(
                f"PyLisp - Error: Attempt to divide by Denominator: {denominator}",
                file=stderr,
            )
            return None

        return self.lhs.eval() / denominator


class LT(BinaryOperator):
    @staticmethod
    def operator_symbol() -> LiteralString:
        return "<"

    def eval(self) -> Boolean:
        return Boolean(self.lhs.eval() < self.rhs.eval())


class EQ(BinaryOperator):
    @staticmethod
    def operator_symbol() -> LiteralString:
        return "=="

    def eval(self) -> Boolean:
        return Boolean(self.lhs.eval() == self.rhs.eval())


class AND(BinaryOperator):
    @staticmethod
    def operator_symbol() -> LiteralString:
        return "&"

    def eval(self) -> Boolean:
        return Boolean(bool(self.lhs.eval()) and bool(self.rhs.eval()))


class OR(BinaryOperator):
    @staticmethod
    def operator_symbol() -> LiteralString:
        return "|"

    def eval(self) -> Boolean:
        return Boolean(bool(self.lhs.eval()) or bool(self.rhs.eval()))


# In[16]:


EvaluatesToBool = Boolean | LT | Constant


class TernaryOperator(Expression):
    def __init__(self, fst: Expression, scnd: Expression, thrd: Expression) -> None:
        self.fst = fst
        self.scnd = scnd
        self.thrd = thrd

    @abstractmethod
    def operator_symbol() -> str:
        pass

    def __repr__(self) -> str:
        return f"({self.operator_symbol()} {self.fst} {self.scnd} {self.thrd})"

    def __str__(self) -> str:  # called for print
        return self.__repr__()


class IfThenElse(TernaryOperator):
    def __init__(
        self,
        fst: EvaluatesToBool,
        scnd: Expression,
        thrd: Expression,
    ) -> None:
        super().__init__(fst, scnd, thrd)

    @staticmethod
    def operator_symbol() -> LiteralString:
        return "IfThenElse"

    def __str__(self) -> str:
        return f"(IF {self.fst} THEN {self.scnd} ELSE {self.thrd})"

    def eval(self) -> Number:
        if self.fst.eval():
            return self.scnd.eval()
        return self.thrd.eval()
