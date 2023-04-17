import ast 
import sys
# from rich.console import Console

def generate_ast(source_code):
    tree = ast.parse(source_code)
    return tree


code = """def greet(name):
    print(f'Hello, {name}!')
greet('World')"""

generate_ast(code)
