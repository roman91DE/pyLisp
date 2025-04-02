from parser import bracket_check, parse_tokens

from tokenizer import tokenize_to_list


def repl() -> None:
    print("Welcome to pyLisp! Type ':q' to quit.")
    while True:
        try:
            line = input(">>> ").strip()
            if line.lower() in {"exit", "quit", ":q"}:
                break
            tokens = tokenize_to_list(line)
            if not bracket_check(tokens):
                print("Error: Unbalanced parentheses.")
                continue
            expr = parse_tokens(tokens)
            if expr is None:
                print("Error: Failed to parse expression.")
                continue
            print(f"Parsed: {expr}")
            print(f"Result: {expr.eval()}")
        except Exception as e:
            print(f"Exception occurred: {e}")


if __name__ == "__main__":
    repl()
