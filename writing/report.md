# Report by Add Your Name(s)
- Ben 
- Bergas
- Daniel 

## Design of your project

: include a diagram

Our program is a translator that accepts Python code and outputs a version that has been translated to JavaScript. The resulting JavaScript program will have the same output and exact same functionality as the original Python program. It can accept different types of programs and different functionalities that Python code has such as for loops, while loops, if statements and more. 

![Diagram](/Diagram_for_CS201.png)
## Implementation of your project

: include information about technical details of your project, including all tools and programming languages used.

The program takes Python code as an input and returns equivalent JavaScript code. It includes a scanner and parser that parses the Python code into a syntax tree, similar to the functionality of parts of the Lox interpreter. The translator part of the program uses the python ast library to making sure to account for all the different kinds of structures, loops, and other features present in our input Python programs. This will convert the Python AST to a JavaScript AST. Then, the main will convert the JavaScript AST into actual JavaScript code using the translator.

## Evaluation and Testing of your Program

: include program input and output and output of test cases in code blocks

### Test 1
Input:
```
# comment
num1 = 5
num2 = 15
# comment2
res = num1 + num2
print(res)
```

Output:
```
//  comment
var num1 = 5;
var num2 = 15;
//  comment2
var res = num1 + num2;
console.log(res);
```

### Test 2
Input:
```
# comments
my_list = [1,2,3,4]
new_list = []
for i in my_list:
    new_list[i] = my_list[i] + 1
print(my_list)
```

Output: 
```
//  comments
var my_list = [1, 2, 3, 4];
var new_list = [];
for (let i = 0; i < my_list.length; i++) {
        new_list[i] = my_list[i] + 1;
}
console.log(my_list);
```

### Test 3
This test is too long to include its input and output in the report, but everything about it works correctly. It can be run with the command `python main.py examples/py3.py`.

: include commands needed to run and test your project

```
python main.py examples/name_of_python_program.py
```

Example1: 
```
python main.py examples/py1.py
```

Example2:
```
python main.py examples/py2.py
```

Example3:
```
python main.py examples/py3.py
```

## Description of the challenges that you faced and how you resolved them

The first thing that was challenges as team was getting used to working with the python ast library and utilize it to the specifies that we were looking for. The main reason is because we do not have the experience with this library, therefore it would need more time in order to use the library, since this is useful on parsing the Python AST to the Javascript AST into the dictionary format based of instances of objects. The next hurdle we faced was at the end after getting the JS ast trying to parse it and work through to get it to a code. The main reason is because we tried using another library for this functionality called `escodegen` which helps translate Javascript AST to code, however we have problem with using the library. We settled on creating the translation manually for each instances inside the Javascript AST. 

## If worked in a team, description of the way in which you and your team members shared the project workload

- Bergas: Worked on `generate_ast.py` on building the nodes and created test cases. Test cases are made using pytest, therefore if want to run the test cases using pytest, has to install pytest on local environment using `pip install pytest`. Nodes are needed to check instances of Python AST to convert to Javascript AST.
- Ben: Worked on `generate_code.py` which handles the part that converts the ast to code. This functionality manually converts instances of the Javascript AST to Javascript code. It can translate expressions of type AssignmentExpression, ExpressionStatement, ForStatement, and Comment.
- Daniel: worked on `Main.py` and `generate_ast.py` with creating node for different functionalities. This functionality drives the whole program as the `main.py` function is the driver program, while also adding functionality to instances of nodes inside `generate_ast.py`.
