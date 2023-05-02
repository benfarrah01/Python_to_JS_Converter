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