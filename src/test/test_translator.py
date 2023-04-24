import ast
import unittest
import GenerateAST


class TestPythonToJavaScriptTranslator(unittest.TestCase):
    # def setUp(self):
    # self.translator = GenerateAST.node_translation()

    def test_simple_expression(self):
        py_code = "x = 2 + 3"
        expected_js_code = "var x = 2 + 3;"
        py_ast = ast.parse(py_code)
        js_ast = self.translator.translate(py_ast)
        js_code = self.translator.generate_code(js_ast)
        self.assertEqual(js_code.strip(), expected_js_code.strip())

    def test_function_call(self):
        py_code = "print('Hello, world!')"
        expected_js_code = "console.log('Hello, world!');"
        py_ast = ast.parse(py_code)
        js_ast = self.translator.translate(py_ast)
        js_code = self.translator.generate_code(js_ast)
        self.assertEqual(js_code.strip(), expected_js_code.strip())

    def test_if_statement(self):
        py_code = "if x > 0:\n    print('Positive')"
        expected_js_code = "if (x > 0) {\n    console.log('Positive');\n}"
        py_ast = ast.parse(py_code)
        js_ast = self.translator.translate(py_ast)
        js_code = self.translator.generate_code(js_ast)
        self.assertEqual(js_code.strip(), expected_js_code.strip())


if __name__ == "__main__":
    unittest.main()
