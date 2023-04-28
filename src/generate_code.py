# Empty list to store translated code
    # Each element is a string representation of a line of code
code = []

def generate(exprlist):
    # Iterate through each tree to get expressions
    for expr in exprlist:
    # Match each expression with its expression type, handle accordingly
        find_expression(expr)
        #print(f"Current: {expr}")

    print()
    # Print each line of translated JavaScript code
    for c in code:
        print(c)


def find_expression(expr):
    if type(expr) == str:
        pass
    elif expr['type'] == 'AssignmentExpression':
        AssignmentExpression(expr)
    elif expr['type'] == 'ExpressionStatement':
        ExpressionStatement(expr)
    elif expr['type'] == 'ForStatement':
        ForStatement(expr)
    elif expr['type'] == 'Comment':
        Comment(expr)


def AssignmentExpression(expr):
    # Variable to control scoping. Default is function-scoped
    scope = "var"

    # code left of operator
    left = ""
    # code right of operator
    right = ""

    # Error handling, because there might not be a previous line in the code
    try:
        # Use block-scoping if the previous line sets up a new block
            # note: IN PROGRESS. Need to make it detect if it's in a block after the first line of a for loop
        if "for" in code[-1]:
            scope = "let"
    except IndexError:
        pass

    # Check if left side is MemberExpression
    if expr['left']['type'] == 'MemberExpression':
        # ("    name[property]")
        left = (f"\t{expr['left']['object']['name']}[{expr['left']['property']['name']}]")

        # If left is MemberExpression and right is BinaryExpression
        if expr['right']['type'] == 'BinaryExpression':
            # Get the BinaryExpression's operator
            operator = expr['right']['operator']
            # ("name2[property] operator [value];")
            right = (f"{expr['right']['left']['object']['name']}[{expr['left']['property']['name']}] {operator} {expr['right']['right']['value']};")

            # Get the entire expression's operator (usually "=")
            operator = expr['operator']

            # Connect the parts to get a finished line of code
            code.append(f"{left} {operator} {right}")
            return

   # Check if left side is Identifier
    elif expr['left']['type'] == 'Identifier':
        # ("scope name")
        left = (f"{scope} {expr['left']['name']}")

    # Check if right side is Identifier
    if expr['right']['type'] == 'Identifier':
        # ("value;")
        right = (f"{expr['right']['value']};")
    
    # Check if right side BinaryExpression
    elif expr['right']['type'] == 'BinaryExpression':
        operator = expr['right']['operator']
        right = (f"{expr['right']['left']['name']} {operator} {expr['right']['right']['name']};")
    
    # Check if right side ArrayExpression
    elif expr['right']['type'] == 'ArrayExpression':
        elements = []
        for i in expr['right']['elements']:
            elements.append(i['value'])
        right = (f"{elements};")

    operator = expr['operator']
    code.append(f"{left} {operator} {right}")
    
    



def ExpressionStatement(expr):
    if expr['expression']['type'] == 'CallExpression':
        code.append(f"console.log({expr['expression']['arguments'][0]['name']});")

def ForStatement(expr):
    body = ""
    init = (f"for (let {expr['init']['name']} = 0; {expr['init']['name']} < {expr['test']['name']}.length; {expr['init']['name']}++)"+" {")
    code.append(init)
    for i in range(len(expr['body'])):
        body = find_expression(expr['body'][i])
            #print(body)
    code.append("}")

# Handle comments
def Comment(expr):
    code.append(f"// {expr['value']}")