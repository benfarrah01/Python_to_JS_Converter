import ast 
import sys

def generate_ast(source_code):
    tree = ast.parse(source_code)
    return tree

source_code = sys.argv[1]