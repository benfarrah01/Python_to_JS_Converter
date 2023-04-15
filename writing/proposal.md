# Informative Title for the Project

Python to Java Translator

## Add Your Name(s)

- Daniel
- Bergas 
- Ben 

## Description of the Main Idea

We will create a translator that accepts Python code and outputs a version that has been translated to JavaScript. The resulting JavaScript program will have the same output and exact same functionality as the original Python program.

## Description of the Tasks that You Will Complete

To create a program that translates Python code to JavaScript code. The program could incorporate aspects of both programming languages, such as data types, loops, and functions. The translator could use a combination of parsing techniques and regular expressions to identify the structure of the Python code and generate the equivalent JavaScript code. To test the program, you could write a set of Python test cases that cover a range of Python features, and then verify that the translated JavaScript code produces the same output as the original Python code.

## Detailed Plan for Your Team to Complete the Project with a Timeline

A high-level overview of the steps involved in building such a translator:

- Develop a parser for Python code using a tool like ANTLR or pyparsing, or create one similar to other existing parsers. This parser should be able to parse Python code into an abstract syntax tree (AST).

- Write a translator that converts our Python AST into a JavaScript AST. In this step, each Python AST node must be mapped to a corresponding JavaScript AST node.

- Generate JavaScript code from the JavaScript AST. The tool escodegen, or other similar tools, can be used for this.

- Write a test suite for the translator. Test to see if the conversion is accurate and if both programs accomplish the same goal in the same way.

- Compare the output of the two programs and ensure they are the same.

 
