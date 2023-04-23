import sys
import ast
#import scanning
import GenerateAST
from pathlib import Path

def main():
    python_file = sys.argv[1]
    python_path = Path(python_file)
    if python_path.is_file():
        python_text = python_path.read_text().splitlines()
        tree = ast.parse(python_path.read_text())
        js_ast = GenerateAST.node_translation(tree)
        print(js_ast)
        #print(python_text)
        #my_scanner = scanning.scanner(python_text)
        #my_scanner.scan()
        

if __name__ == "__main__":
    main()


def generate_code(node):
    if node['type'] == 'Program':
        return generate_code(node['body'])
    elif node['type'] == 'BlockStatement':
        return '{\n' + '\n'.join([generate_code(child) for child in node['body']]) + '\n}'
    elif node['type'] == 'VariableDeclaration':
        return f'{node["kind"]} {generate_code(node["declarations"][0])};'
    elif node['type'] == 'VariableDeclarator':
        return f'{node["id"]["name"]} = {generate_code(node["init"])}'
    elif node['type'] == 'Literal':
        return str(node['value'])
    elif node['type'] == 'CallExpression':
        args = ', '.join([generate_code(arg) for arg in node['arguments']])
        return f'{generate_code(node["callee"])}({args})'
    elif node['type'] == 'Identifier':
        return node['name']
    else:
        raise NotImplementedError(f'Unsupported node type: {node["type"]}')

