# 🐍 pyLisp

**pyLisp** is a minimal Lisp REPL environment written entirely in pure Python.  
It supports basic arithmetic and logical expressions using a Lisp-like syntax, all built from scratch with Python's standard library.

---

## ✨ Features

- Lisp-style prefix notation:
  - `( + 1 2 )` → `3`
  - `( < 3 5 )` → `True`
  - `( IfThenElse ( < 1 2 ) 10 20 )` → `10`
- Strongly typed internal expression tree using `@dataclass` and `abc`
- Tokenizer, parser, and expression evaluation pipeline
- Clean and extensible architecture

---

## 🧪 Example Usage

```bash
$ python -m repl
Welcome to pyLisp! Type ':q' to quit.
>>> ( + 3 4 )
Parsed: (+ 3 4)
Result: 7
>>> ( IfThenElse ( < 5 3 ) 42 99 )
Parsed: (IF (5 < 3) THEN 42 ELSE 99)
Result: 99



⸻

🗂️ Project Structure

src/
├── repl.py         # REPL interface
├── parser.py       # S-expression parser
├── tokenizer.py    # Custom tokenizer
├── symbols.py      # Operator definitions
├── expression.py   # Expression classes and evaluation logic
└── notebooks/      # Development notebooks for prototyping



⸻

🧰 Requirements
	•	Python 3.10+ (tested with 3.13)
	•	No third-party dependencies

⸻

🚀 Getting Started

Clone the repository and run the REPL:

git clone https://github.com/roman91DE/pyLisp.git
cd pyLisp/src
python -m repl



⸻

📚 Roadmap Ideas
	•	Add support for more operators (e.g., *, /, ==)
	•	Implement let-bindings or simple variable environments
	•	Pretty printing and error diagnostics
	•	Web REPL (e.g., using Flask or FastAPI)

⸻

📝 License

MIT License. See LICENSE for details.

⸻

Made with ❤️ and Python.
