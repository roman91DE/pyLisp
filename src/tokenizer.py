from collections.abc import Iterable
from string import whitespace

import symbols


def tokenizer(s: str) -> Iterable[str]:
    """Tokenizes an Expression String into its single Tokens"""
    tokens, acc = [], []

    for c in s:
        if c in whitespace:
            tokens.append("".join(acc))
            acc.clear()
        elif c in symbols.operators.union(symbols.parens):
            tokens.append("".join(acc))
            acc.clear()
            tokens.append(c)
        else:
            acc += c

    return filter(lambda s: len(s) > 0, tokens)


def tokenize_to_list(s: str) -> list[str]:
    return list(tokenizer(s))
