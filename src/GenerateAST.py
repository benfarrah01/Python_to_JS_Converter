import ast 
import sys
# from rich.console import Console

operator_map = {
    ast.Add: '+',
    ast.Sub: '-',
    ast.Mult: '*',
    ast.Div: '/',
    ast.Mod: '%',
    ast.Pow: '**',
    ast.BitAnd: '&',
    ast.BitOr: '|',
    ast.BitXor: '^',
    ast.LShift: '<<',
    ast.RShift: '>>',
    ast.FloorDiv: '//'
}

def node_translation(node):
    if isinstance(node, ast.Module):
        return {'type': 'Program', 'body': [node_translation(child) for child in node.body]} 
    elif isinstance(node, ast.FunctionDef):
        return {'type': 'FunctionDeclaration', 'id': node.name, 'params': [node_translation(arg) for arg in node.args.args], 'body': [node_translation(child) for child in node.body]}
    elif isinstance(node, ast.Return):
        return {'type': 'ReturnStatement', 'argument': node_translation(node.value)}
    elif isinstance(node, ast.Expr):
        return{'type': 'ExpressionStatement', 'expression': node_translation(node.value)}
    elif isinstance(node, ast.Call):
        return{'type': 'CallExpression', 'callee': node_translation(node.func), 'arguments': [node_translation(arg) for arg in node.args]}
    elif isinstance(node, ast.Name):
        return {'type': 'Identifier', 'name': node.id}
    elif isinstance(node, ast.arg):
        return {'type': 'Identifier', 'name': node.arg}
    elif isinstance(node, ast.JoinedStr):
        elements = []
        for n in node.values:
            if isinstance(node, ast.Str):
                elements.append({'type': 'Literal', 'value': n.s})
            elif isinstance(node, ast.FormattedValue):
                elements.append(node_translation(n))
        return {'type': 'BinaryExpression', 'operator': '+', 'left': node_translation(node.values[0]), 'right': node_translation(node.values[1]) if len(elements) > 1 else None}
    elif isinstance(node, ast.Str):
        return {'type': 'Literal', 'value': node.s}
    elif isinstance(node, ast.Num):
        return {'type': 'Identifier', 'value': node.n}
    elif isinstance(node, ast.Constant):
        return {'type': 'Literal', 'value': node.value}
    elif isinstance(node, ast.BoolOp):
        operator_op = {ast.And: '&&', ast.Or: '||'}
        operator = operator_op[node.op.__class__]
        return {'type': 'LogicalExpression', 'operator': operator, 'left': node_translation(node.values[0]), 'right': node_translation(node.values[1])}
    elif isinstance(node, ast.BinOp):
        return {'type': 'BinaryExpression', 'operator': operator_map[node.op.__class__], 'left': node_translation(node.left), 'right': node_translation(node.right)}
    else:
        raise Exception(f'Unsupported node type: {type(node).__name__}')
    

source_code = """
def greet(name):
    print(f'Hello, {name}!')
    
greet('World')"""

tree = ast.parse(source_code)
js_ast = node_translation(tree)

