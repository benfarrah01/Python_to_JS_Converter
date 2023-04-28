import sys
import ast
import generate_ast
import generate_code
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
    # Get argument from command
        # arg is the path of the Python file to be translated
    python_file = sys.argv[1]

    # Convert argument to path variable
    python_path = Path(python_file)

    # Check if the path leads to a file
    if python_path.is_file():
        # Read the text from the file, store in string. Parse the string to get a Module object (from AST).
        text = python_path.read_text()
        tree = ast.parse(text)

        # Pass tree into node_translation() to get AST
        js_ast = generate_ast.node_translation(tree)

        # create list of strings, each element is a line from the original python code
        textlist = text.splitlines()

        # create list of expressions
        exprlist = []
        for key in js_ast:
            for expr in js_ast[key]:
                # Print expression for testing purposes, DELETE THIS LINE LATER
                if type(expr) == str:
                    pass
                else:
                    exprlist.append(expr)
                    

        # add commented lines to list of expressions
        for i in range(len(textlist)):
            if "#" in textlist[i]:
                exprlist.insert(i, {
                    "type": "Comment",
                    "value": textlist[i].replace("#","")
                })


        # Pass AST into generate() to get translated JavaScript code
        generate_code.generate(exprlist)


if __name__ == "__main__":
    main()
