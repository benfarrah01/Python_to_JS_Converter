import escodegen
import GenerateAST

class jscodegenerator():
    def generate(self, node):
        return escodegen.generate(node)
    
code_generator = jscodegenerator
js_code = jscodegenerator.generate(code_generator)