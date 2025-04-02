from argparse import ArgumentParser

from parser import bracket_check, parse_tokens
from tokenizer import tokenize_to_list


def evaluate_expression(expr_str: str) -> None:
    tokens = tokenize_to_list(expr_str)
    if not bracket_check(tokens):
        print("Error: Unbalanced parentheses.")
        return
    expr = parse_tokens(tokens)
    if expr is None:
        print("Error: Failed to parse expression.")
        return
    print(f"Expression: {expr}")
    print(f"Result: {expr.eval()}")


def repl() -> None:
    print("Welcome to pyLisp! Type ':q' to quit.")
    while True:
        try:
            line = input(">>> ").strip()
            if line.lower() in {"exit", "quit", ":q"}:
                break
            evaluate_expression(line)
        except Exception as e:
            print(f"Exception occurred: {e}")


if __name__ == "__main__":
    parser = ArgumentParser(
        description="pyLisp - A minimal Lisp-like evaluator in Python",
    )
    parser.add_argument(
        "file",
        nargs="?",
        help="Path to a file containing a pyLisp expression",
    )
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Start REPL mode",
    )

    args = parser.parse_args()

    if args.file and not args.interactive:
        try:
            with open(args.file, encoding="utf-8") as f:
                content = f.read().strip()
                evaluate_expression(content)
        except Exception as e:
            print(f"Exception occurred while processing file: {e}")
    else:
        repl()
