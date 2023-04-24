import sys
import ast
import escodegen

# import scanning
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

"""
def translate(node):
    if "type" not in node.keys():
        return ""
    elif node["type"] == "Identifier":
        return node["name"]
    elif node["type"] == "Literal":
        return str(node["value"])
    elif node["type"] == "BinaryExpression":
        return (
            f"({translate(node['left'])} {node['operator']} {translate(node['right'])})"
        )
    elif node["type"] == "UnaryExpression":
        return f"({node['operator']} {translate(node['argument'])})"
    elif node["type"] == "BlockStatement":
        return "\n".join([translate(child) for child in node["body"]])
    elif node["type"] == "WhileStatement":
        return f"while ({translate(node['test'])}) {{\n{translate(node['body'])}\n}}"
    elif node["type"] == "IfStatement":
        return f"if ({translate(node['test'])}) {{\n{translate(node['consequent'])}\n}}{'else {'+translate(node['alternate'])+'}' if node['alternate'] else ''}"
    elif node["type"] == "BreakStatement":
        return "break;"
    elif node["type"] == "AssignmentExpression":
        return f"{translate(node['left'])} = {translate(node['right'])}"
    elif node["type"] == "ForStatement":
        init = translate(node["init"]) if "init" in node else ""
        test = translate(node["test"]) if "test" in node else ""
        update = translate(node["update"]) if "update" in node else ""
        return f"for ({init}; {test}; {update}) {{\n{translate(node['body'])}\n}}"
    elif node["type"] == "ArrayExpression":
        return f"[{', '.join([translate(child) for child in node['elements']])}]"
    else:
        return ""
"""


def main():
    python_file = sys.argv[1]
    python_path = Path(python_file)
    if python_path.is_file():
        python_text = python_path.read_text().splitlines()
        tree = ast.parse(python_path.read_text())
        js_ast = GenerateAST.node_translation(tree)
        final_code = translate(js_ast)
        print(final_code)
        # print(python_text)
        # my_scanner = scanning.scanner(python_text)
        # my_scanner.scan()
        # Generate JavaScript code from the AST


if __name__ == "__main__":
    main()
