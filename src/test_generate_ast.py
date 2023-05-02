import pytest
import ast
from generate_ast import node_translation

def test_moduletranslation():
    node = ast.parse("x = 1")
    expected_output = {
    "type": "Program",
    "body": [
        {
            "type": "AssignmentExpression",
            "operator": "=",
            "left": {"type": "Identifier", "name": "x"},
            "right": {"type": "Identifier", "value": 1}
        }
    ],
}
    assert node_translation(node) == expected_output

def test_FunctionDef_translation():
    node = ast.parse("""
def add(a, b):
    return a + b
    """).body[0]

    expected_output = {
        "type": "FunctionDeclaration",
        "id": "add", 
        "params":[
            {"type": "Identifier", "name": "a"},
            {"type": "Identifier", "name": "b"}
        ],
        "body":[
            {
                "type": "ReturnStatement",
                "argument": {
                    "type": "BinaryExpression",
                    "operator": "+",
                    "left": {"type": "Identifier", "name": "a"},
                    "right": {"type": "Identifier", "name": "b"}
                }
            }
        ]  
    }

    assert node_translation(node) == expected_output

def test_BoolOp_translation():
    tree = ast.parse("x and y or z")
    boolop_node = tree.body[0].value
    result = node_translation(boolop_node)
    
    expected_output = {
        "type": "LogicalExpression",
        "operator": "||",
        "left": {
            "type": "LogicalExpression",
            "operator": "&&", 
            "left": {"type": "Identifier", "name": "x"},
            "right": {"type": "Identifier", "name": "y"},
        },
        "right": {"type": "Identifier", "name": "z"},
    }

    assert result == expected_output

def test_BinOp_translation():
    binop_node = ast.BinOp(
        left = ast.Num(n = 5),
        op = ast.Add(),
        right = ast.Num(n = 8)
    )

    output = node_translation(binop_node)

    expected_output = {
        "type": "BinaryExpression",
        "operator": "+",
        "left": {"type": "Identifier", "value": 5},
        "right": {"type": "Identifier", "value": 8}
    }

    assert output == expected_output

def test_UnaryOp_translation():
    node = ast.parse("-a").body[0].value
    result = node_translation(node)

    expected_output = {
        "type": "UnaryExpression",
        "operator": "-",
        "argument": {"type": "Identifier", "name": "a"}
    }

    assert result == expected_output

def test_For_translation():
    node = """
for i in range(10):
    print(i)
    """

    parsed_code = ast.parse(node)
    result = node_translation(parsed_code.body[0])

    expected_output = {
        "type": "ForStatement",
        "init": {"type": "Identifier", "name": "i"},
        "test":{
            "type": "CallExpression",
            "callee": {"type": "Identifier", "name": "range"},
            "arguments": [{"type": "Identifier", "value": 10}],
        },
        "body":[
            {
                "type": "ExpressionStatement",
                "expression": {
                    "type": "CallExpression", 
                    "callee": {"type": "Identifier", "name": "print"},
                    "arguments": [{"type": "Identifier", "name": "i"}]
                },
            }
        ],
        "update": None,
    }

    assert result == expected_output

def test_node_translation_while():

    code = """
while i < 10:
    i += 1
    """
    node = ast.parse(code).body[0]

    result = node_translation(node)

    expected = {
        "type": "WhileStatement",
        "test": {
            "type": "BinaryExpression",
            "operator": "<",
            "left": {"type": "Identifier", "name": "i"},
            "right": {"type": "Identifier", "value": 10},
        },
        "body": [
            {
                # "type": "ExpressionStatement",
                # "expression": {
                #     "type": "AssignmentExpression",
                #     "operator": "+=",
                #     "left": {"type": "Identifier", "name": "i"},
                #     "right": {"type": "Literal", "value": 1},
                # },
                "type": "AssignmentExpression",
                "operator": "+=",
                "left": {"type": "Identifier", "name": "i"},
                "right": {"type": "Identifier", "value": 1},
            }
        ],
    }

    assert result == expected
