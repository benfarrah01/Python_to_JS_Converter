import sys
import ast
#import escodegen

# import scanning
import generate_code
import GenerateAST
from pathlib import Path


# Sample JavaScript AST as a Python dictionary
ast_node = {
    "type": "Program",
    "body": [
        {
            "type": "VariableDeclaration",
            "kind": "let",
            "declarations": [
                {
                    "type": "VariableDeclarator",
                    "id": {"type": "Identifier", "name": "x"},
                    "init": {"type": "Literal", "value": 42},
                },
            ],
        },
        {
            "type": "ExpressionStatement",
            "expression": {
                "type": "CallExpression",
                "callee": {"type": "Identifier", "name": "console.log"},
                "arguments": [
                    {"type": "Identifier", "name": "x"},
                ],
            },
        },
    ],
}



def main():
    python_file = sys.argv[1]
    python_path = Path(python_file)
    if python_path.is_file():
        python_text = python_path.read_text().splitlines()
        tree = ast.parse(python_path.read_text())
        js_ast = GenerateAST.node_translation(tree)
        generate_code.generate_code(js_ast)
        #final_code = translate(js_ast)
        #print(final_code)
        # print(python_text)
        # my_scanner = scanning.scanner(python_text)
        # my_scanner.scan()
        # Generate JavaScript code from the AST


if __name__ == "__main__":
    main()
