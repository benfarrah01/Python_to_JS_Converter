"""
This module contains a Python to JavaScript converter using the Abstract Syntax Tree (AST) of Python.

The `node_translation` function in this module takes an AST node of Python and returns equivalent JavaScript AST node.
The JavaScript AST node is represented as a Python dictionary with keys such as "type", "id", "params", "body", "argument", etc.

The `operator_map` dictionary maps Python operators to their equivalent JavaScript operators, and the `js_ops` dictionary maps Python comparison operators to their equivalent JavaScript operators.

Usage:
    The `node_translation` function can be called with any valid Python AST node given from its equivalent Python Code as an argument to obtain its equivalent JavaScript AST node.

"""


import ast
import sys

operator_map = {
    ast.Add: "+",
    ast.Sub: "-",
    ast.USub: "-",
    ast.Mult: "*",
    ast.Div: "/",
    ast.Mod: "%",
    ast.Pow: "**",
    ast.BitAnd: "&",
    ast.BitOr: "|",
    ast.BitXor: "^",
    ast.LShift: "<<",
    ast.RShift: ">>",
    ast.FloorDiv: "//",
}

js_ops = {
    ast.Eq: "=",
    ast.NotEq: "!=",
    ast.Lt: "<",
    ast.LtE: "<=",
    ast.Gt: ">",
    ast.GtE: ">=",
    ast.Is: "===",
    ast.IsNot: "!==",
    ast.In: "In",
    ast.NotIn: "not in",
}

def node_translation(node):
    # Module Node
    if isinstance(node, ast.Module):
        return {
            "type": "Program",
            "body": [node_translation(child) for child in node.body],
        }
    # Function Declaration Node, where it checks for the name, parameters and body of function
    elif isinstance(node, ast.FunctionDef):
        return {
            "type": "FunctionDeclaration",
            "id": node.name,
            "params": [node_translation(arg) for arg in node.args.args],
            "body": [node_translation(child) for child in node.body],
        }
    # Return statements, checks for the value or the argument
    elif isinstance(node, ast.Return):
        return {"type": "ReturnStatement", "argument": node_translation(node.value)}
    # Expression statements, checks for expression of statemtn
    elif isinstance(node, ast.Expr):
        return {
            "type": "ExpressionStatement",
            "expression": node_translation(node.value),
        }
    # Call Expression, checks for callee, arguments inside of callee
    elif isinstance(node, ast.Call):
        return {
            "type": "CallExpression",
            "callee": node_translation(node.func),
            "arguments": [node_translation(arg) for arg in node.args],
        }
    # Name of node, regardless of the instance of the name
    elif isinstance(node, ast.Name):
        return {"type": "Identifier", "name": node.id}
    # Argument of node, regardless of the statements
    elif isinstance(node, ast.arg):
        return {"type": "Identifier", "name": node.arg}
    # Joined String method or string concatenation
    elif isinstance(node, ast.JoinedStr):
        elements = []
        for n in node.values:
            if isinstance(node, ast.Str):
                elements.append({"type": "Literal", "value": n.s})
            elif isinstance(node, ast.FormattedValue):
                elements.append(node_translation(n))
        return {
            "type": "BinaryExpression",
            "operator": "+",
            "left": node_translation(node.values[0]),
            "right": node_translation(node.values[1]) if len(elements) > 1 else None,
        }
    # String node, literal type
    elif isinstance(node, ast.Str):
        return {"type": "Literal", "value": node.s}
    # Number node, Identifier type
    elif isinstance(node, ast.Num):
        return {"type": "Identifier", "value": node.n}
    # Constant node, Literal type
    elif isinstance(node, ast.Constant):
        return {"type": "Literal", "value": node.value}
    # Boolean operations, checks between left, right values and operator. Return true or false
    elif isinstance(node, ast.BoolOp):
        operator_op = {ast.And: "&&", ast.Or: "||"}
        operator = operator_op[node.op.__class__]
        return {
            "type": "LogicalExpression",
            "operator": operator,
            "left": node_translation(node.values[0]),
            "right": node_translation(node.values[1]),
        }
    # Binary operations, checks between left, right values and operator.
    elif isinstance(node, ast.BinOp):
        return {
            "type": "BinaryExpression",
            "operator": operator_map[node.op.__class__],
            "left": node_translation(node.left),
            "right": node_translation(node.right),
        }
    # Compare operations, checks between left, right and operator.
    elif isinstance(node, ast.Compare):
        left = node_translation(node.left)
        ops = [js_ops[op.__class__] for op in node.ops]
        comparators = [node_translation(comp) for comp in node.comparators]
        op = " ".join(ops)
        right = comparators[0]
        if len(comparators) > 1:
            for i in range(1, len(comparators)):
                op_node = ops[i - 1]
                right_node = comparators[i]
                op = f"{op} {op_node} {right_node}"
        return {
            "type": "BinaryExpression",
            "left": left,
            "operator": op,
            "right": right,
        }

    elif isinstance(node, ast.For):
        return {
            "type": "ForStatement",
            "init": node_translation(node.target),
            "test": node_translation(node.iter),
            "body": [node_translation(child) for child in node.body],
            "update": None,
        }
    # Assign
    elif isinstance(node, ast.Assign):
        return {
            "type": "AssignmentExpression",
            "operator": "=",
            "left": node_translation(node.targets[0]),
            "right": node_translation(node.value),
        }

    elif isinstance(node, ast.While):
        return {
        "type": "WhileStatement",
        "test": node_translation(node.test),
        "body": [node_translation(child) for child in node.body],
    }

    elif isinstance(node, ast.Break):
        return {"type": "BreakStatement"}
    elif isinstance(node, ast.Continue):
        return {"type": "ContinueStatement"}

    # If statements
    elif isinstance(node, ast.If):
        return {
            "type": "IfStatement",
            "test": node_translation(node.test),
            "consequent": [node_translation(child) for child in node.body],
            "alternate": node_translation(node.orelse[0]) if node.orelse else None,
        }

    elif isinstance(node, ast.List):
        return {
            "type": "ArrayExpression",
            "elements": [node_translation(element) for element in node.elts],
        }

    elif isinstance(node, ast.UnaryOp):
        return {
            "type": "UnaryExpression",
            "operator": operator_map[node.op.__class__],
            "argument": node_translation(node.operand),
        }

    elif isinstance(node, ast.Subscript):
        return {
            "type": "MemberExpression",
            "object": node_translation(node.value),
            "property": node_translation(node.slice),
            "computed": True,
        }
    elif isinstance(node, ast.AugAssign):
        return {
        "type": "AssignmentExpression",
        "operator": operator_map[node.op.__class__] + "=",
        "left": node_translation(node.target),
        "right": node_translation(node.value),
    }
    else:
        raise Exception(f"Unsupported node type: {type(node).__name__}")

