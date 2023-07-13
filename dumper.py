import qastle
from pathlib import Path
import ast

q_text = Path("test.txt").read_text()

my_ast = qastle.text_ast_to_python_ast(q_text)

print(ast.dump(my_ast, indent=2))
