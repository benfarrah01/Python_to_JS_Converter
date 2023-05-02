import pytest
import generate_code

def test_generate_returns_translated_AssignmentExpression_left_identifier_right_identifier():
    expr = [
        {
            "type": "AssignmentExpression",
            "operator": "=",
            "left": {"type": "Identifier", "name": "x"},
            "right": {"type": "Identifier", "value": 1}
        }
        ]
    expected_output = ["var x = 1;"]
    output = generate_code.generate(expr)

    # reset global variable
    generate_code.code = []

    assert output == expected_output

def test_generate_returns_translated_AssignmentExpression_left_identifier_right_BinaryExpression():
    expr = [
        {'type': 'AssignmentExpression', 'operator': '=', 'left': {'type': 'Identifier', 'name': 'num1'}, 'right': {'type': 'Identifier', 'value': 5}},
        {'type': 'AssignmentExpression', 'operator': '=', 'left': {'type': 'Identifier', 'name': 'num2'}, 'right': {'type': 'Identifier', 'value': 15}},
        {'type': 'AssignmentExpression', 'operator': '=', 'left': {'type': 'Identifier', 'name': 'res'}, 'right': {'type': 'BinaryExpression', 'operator': '+', 'left': {'type': 'Identifier', 'name': 'num1'}, 'right': {'type': 'Identifier', 'name': 'num2'}}}
    ]
    expected_output = [
        "var num1 = 5;",
        "var num2 = 15;",
        "var res = num1 + num2;"
    ]
    output = generate_code.generate(expr)

    # reset global variable
    generate_code.code = []

    assert output == expected_output

def test_generate_returns_translated_AssignmentExpression_left_identifier_right_ArrayExpression():
    expr = [
        {'type': 'AssignmentExpression', 'operator': '=', 'left': {'type': 'Identifier', 'name': 'my_list'}, 'right': {'type': 'ArrayExpression', 'elements': [{'type': 'Identifier', 'value': 1}, {'type': 'Identifier', 'value': 2}, {'type': 'Identifier', 'value': 3}, {'type': 'Identifier', 'value': 4}]}}
    ]
    
    expected_output = ["var my_list = [1, 2, 3, 4];"]
    output = generate_code.generate(expr)

    # reset global variable
    generate_code.code = []

    assert output == expected_output

def test_generate_returns_translated_ExpressionStatement():
    expr = [
        {'type': 'AssignmentExpression', 'operator': '=', 'left': {'type': 'Identifier', 'name': 'h'}, 'right': {'type': 'Identifier', 'value': 5}},
        {'type': 'ExpressionStatement', 'expression': {'type': 'CallExpression', 'callee': {'type': 'Identifier', 'name': 'print'}, 'arguments': [{'type': 'Identifier', 'name': 'h'}]}}
    ]

    expected_output = [
        "var h = 5;",
        "console.log(h);"
        ]
    output = generate_code.generate(expr)

    # reset global variable
    generate_code.code = []

    assert output == expected_output

def test_generate_returns_translated_ForStatement():
    expr = [
        {
            'type': 'ForStatement', 
            'init': {
                'type': 'Identifier',
                'name': 'i'
                }, 
            'test': {
                'type': 'Identifier', 
                'name': 'my_list'
                }, 
            'body': [
                {
                    'type': 'AssignmentExpression', 
                    'operator': '=', 
                    'left': {
                        'type': 'MemberExpression', 
                        'object': {
                            'type': 'Identifier', 
                            'name': 'new_list'
                            }, 
                        'property': {
                            'type': 'Identifier', 
                            'name': 'i'
                            }, 
                        'computed': True
                        }, 
                    'right': {
                        'type': 'BinaryExpression', 
                        'operator': '+', 
                        'left': {
                            'type': 'MemberExpression', 
                            'object': {
                                'type': 'Identifier', 
                                'name': 'my_list'
                                }, 
                            'property': {
                                'type': 'Identifier', 
                                'name': 'i'
                                }, 
                            'computed': True
                            }, 
                        'right': {
                            'type': 'Identifier', 
                            'value': 1
                            }
                        }
                    }
                ], 
            'update': None
        }
    ]
    expected_output = [
        "for (let i = 0; i < my_list.length; i++) {",
        "\tnew_list[i] = my_list[i] + 1;",
        "}"
        ]
    output = generate_code.generate(expr)

    # reset global variable
    generate_code.code = []

    assert output == expected_output

def test_generate_returns_translated_Comment():
    expr = [
        {'type': 'Comment', 'value': 'comment'}
    ]
    expected_output = ["// comment"]
    output = generate_code.generate(expr)

    # reset global variable
    generate_code.code = []

    assert output == expected_output