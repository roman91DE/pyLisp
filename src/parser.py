#!/usr/bin/env python

# In[48]:


from numbers import Number

import expression

# In[58]:


def bracket_check(tokens: list[str]) -> bool:
    op, cl = 0, 0
    for token in tokens:
        if token == "(":
            op += 1
        elif token == ")":
            cl += 1
        if cl > op:
            return False
    if op != cl:
        return False

    return True


# In[51]:


symbols_lookup = {
    "+": (expression.Addition, 2),
    "-": (expression.Subtraction, 2),
    "*": (expression.Multiplication, 2),
    "/": (expression.Division, 2),
    "<": (expression.LT, 2),
    "==": (expression.EQ, 2),
    "&": (expression.AND, 2),
    "|": (expression.OR, 2),
    "!": (expression.NOT, 1),
    "IfThenElse": (expression.IfThenElse, 3),
}


# In[52]:


def cast_string_to_scalar(s: str) -> Number | None:
    def _scalar_string_cast(s: str) -> int | float | bool:
        if s.lower() in ("true", "false"):
            return s.lower() == "true"
        if "." in s.lower():
            return float(s)
        return int(s)

    try:
        return _scalar_string_cast(s)
    except ValueError:
        return None


def parse_argument(token: str) -> expression.Expression | None:
    val = cast_string_to_scalar(token)
    if val is None:
        return None
    if isinstance(val, bool):
        return expression.Boolean(val)
    return expression.Constant(val)


def parse_argument_list(tokens: list[str]) -> list[expression.Expression] | None:
    args = []
    i = 0
    while i < len(tokens):
        if tokens[i] == "(":
            depth = 1
            j = i + 1
            while j < len(tokens) and depth > 0:
                if tokens[j] == "(":
                    depth += 1
                elif tokens[j] == ")":
                    depth -= 1
                j += 1
            subexpr = tokens[i:j]
            parsed = parse_tokens(subexpr)
            if parsed is None:
                return None
            args.append(parsed)
            i = j
        else:
            parsed = parse_argument(tokens[i])
            if parsed is None:
                return None
            args.append(parsed)
            i += 1
    return args


# In[53]:


def parse_tokens(tokens: list[str]) -> expression.Expression | None:
    if tokens[0] != "(" or tokens[-1] != ")":
        return None

    if len(tokens) == 1:
        return parse_argument(tokens[0])

    tokens = tokens[1:-1]
    if len(tokens) == 0:
        return expression.Empty()

    symbol = tokens[0]
    op_class, arity = symbols_lookup.get(symbol, (None, None))
    if op_class is None:
        return None

    args = parse_argument_list(tokens[1:])
    if args is None or len(args) != arity:
        return None

    return op_class(*args)
