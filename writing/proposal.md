# Informative Title for the Project

Python to Java Translator

## Add Your Name(s)

- Daniel
- Bergas 
- Ben 

## Description of the Main Idea

We will create a translator that accepts Python code and outputs a version that has been translated to Java. The resulting Java program will have the same output and exact same functionality as the original Python program.

## Description of the Tasks that You Will Complete

We will create a program which accepts Python code as an input and returns equivalent Java code. We will first need to develop a scanner and parser whiich can parse the Python code into a syntax tree, similar to the functionality of parts of the Lox interpreter. We will then need to actually create the translator, making sure to account for all the different kinds of structures, loops, and other features present in our input Python programs. This will convert our Python AST to a Java AST. We will then convert the Java AST into actual Java code, which should have the same output as the original Python program.

## Detailed Plan for Your Team to Complete the Project with a Timeline

1. Develop a scanner and parser for Python code using a tool like ANTLR or pyparsing, or create ones similar to other existing scanners and parsers. These should be able to parse Python code into an abstract syntax tree (AST).

2. Write a translator that converts our Python AST into a Java AST. In this step, each Python AST node must be mapped to a corresponding Java AST node.

3. Generate Java code from the Java AST. The tool escodegen, or other similar tools, can be used for this.

4. Write a test suite for the translator. Test to see if the conversion is accurate and if both programs accomplish the same goal in the same way. Compare the output of the two programs and ensure they are the same.

 
