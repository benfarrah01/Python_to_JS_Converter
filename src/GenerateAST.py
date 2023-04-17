import ast 
import sys
# from rich.console import Console

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
    elif isinstance(node, ast.Str):
        return {'type': 'Literal', 'value': node.s}
    elif isinstance(node, ast.Num):
        return {'type': 'Identifier', 'name': node.n}
    else:
        raise Exception(f'Unsupported node type: {type(node).__name__}')
    

source_code = """
def greet(name):
    print(f'Hello, {name}!')
    
greet('World')"""

tree = ast.parse(source_code)
js_ast = node_translation(tree)

