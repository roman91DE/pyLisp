from string import whitespace
from typing import Iterable

import symbols


def tokenizer(s: str) -> Iterable[str]:
    tokens, acc = [], []

    for c in s:
        if c in whitespace:
            tokens.append("".join(acc))
            acc.clear()
        elif c in symbols.operators or c in symbols.parens:
            tokens.append("".join(acc))
            acc.clear()
            tokens.append(c)
        else:
            acc += c

    return filter(lambda s: len(s) > 0, tokens)


def tokenize_to_list(s: str) -> list[str]:
    return list(tokenizer(s))
