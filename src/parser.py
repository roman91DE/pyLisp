#!/usr/bin/env python
# coding: utf-8

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
    "<": (expression.LT, 2),
    "IfThenElse": (expression.IfThenElse, 3),
}


# In[52]:


def cast_string_to_scalar(s: str) -> Number | None:
    def _scalar_string_cast(s: str) -> int | float | bool:
        if s.lower() in ("true", "false"):
            return s.lower() == "true"
        elif "." in s.lower():
            return float(s)
        else:
            return int(s)

    try:
        return _scalar_string_cast(s)
    except ValueError:
        return None


# In[53]:


def parse_tokens(tokens: list[str]) -> expression.Expression | None:
    if tokens[0] != "(" or tokens[-1] != ")":
        return None  # instead of assert

    # Handle atomic values
    if len(tokens) == 1:
        val = cast_string_to_scalar(tokens[0])
        if val is None:
            return None
        if isinstance(val, bool):
            return expression.Boolean(val)
        else:
            return expression.Constant(val)

    # Handle compound expression
    tokens = tokens[1:-1]  # <- moved here, only for compound expressions

    symbol = tokens[0]
    op_class, arity = symbols_lookup.get(symbol, (None, None))
    if op_class is None:
        return None

    args = []
    i = 1
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
            val = cast_string_to_scalar(tokens[i])
            if val is None:
                return None
            if isinstance(val, bool):
                args.append(expression.Boolean(val))
            else:
                args.append(expression.Constant(val))
            i += 1

    if len(args) != arity:
        return None

    return op_class(*args)
