# Report by Add Your Name(s)
- Ben 
- Bergas
- Daniel 

## Design of your project

TODO: include a diagram

Our program is a translator that accepts Python code and outputs a version that has been translated to JavaScript. The resulting JavaScript program will have the same output and exact same functionality as the original Python program.

## Implementation of your project

TODO: include information about technical details of your project, including all tools and programming languages used.

The program takes Python code as an input and returns equivalent JavaScript code. It inlcudes a scanner and parser that parses the Python code into a syntax tree, similar to the functionality of parts of the Lox interpreter.The translator part of the prgram uses the python ast libray to making sure to account for all the different kinds of structures, loops, and other features present in our input Python programs. This will convert the Python AST to a JavaScript AST. Then, the main will convert the JavaScript AST into actual JavaScript code using the translotor.

## Evaluation and Testing of your Program

TODO: include program input and output and output of test cases in code blocks

TODO: include commands needed to run and test your project

## Description of the challenges that you faced and how you resolved them

The first thing that was chanllenges as team was getting used to working with the python ast library and utilize it to the speficies that we were looking for. The next Hardle we faced was at end after getting the JS ast trying to pasre it and work through to get it to a code.

## If worked in a team, description of the way in which you and your team members shared the project workload

Bergas: Worked on generate_ast on building the nodes and created test cases. 
Ben: Worked on Generate_code which handle the part that converts the ast to code.
Daniel: worked on Main and genrate_ast with creating node for differnt fucntionalilies. 
