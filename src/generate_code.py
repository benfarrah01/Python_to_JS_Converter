variables = []
js = {
    "variables": {
        "names": [],
        "values": []
    },
    "expressions": {
    }

}
code = []

def generate_code(tree):

    for key in tree:
        for expr in tree[key]:
            print(expr)
            print()
            find_expression(expr)

    # create variable initialization line
    names = js["variables"]["names"]
    print()
    for c in code:
        print(c)
    
    # print(names)
    # for i in range(len(names)-1):
    #     code[0] = code[0]+(names[i]+", ")
    # code[0] = code[0]+(names[i+1]+";")
    # print(code)
    # print(js["variables"]["values"])

    # # give variables values
    # i = 0
    # values = js["variables"]["values"]
    # for i in range(len(names)-1):
    #     code.append(f"{names[i]} = {values[i]}")
    # print()
    # for c in code:
    #     print(c)

# def get_variables(tree):
#     # find variables, put in list
#     for key in tree:
#         for expr in tree[key]:
#             print(expr)
#             print()
#             if type(expr) == str:
#                 pass
#             else:
#                 names_vals(expr)

def find_expression(expr):
    if type(expr) == str:
        pass
    elif expr['type'] == 'AssignmentExpression':
        code.append(AssignmentExpression(expr))
    elif expr['type'] == 'ExpressionStatement':
        code.append(ExpressionStatement(expr))
    elif expr['type'] == 'ForStatement':
        ForStatement(expr)

def AssignmentExpression(expr):
    # Variable to control scoping. Default is function-scoped
    scope = "var"
    # Error handling, because there might not be a previous line in the code
    try:
        # Use block-scoping if the previous line sets up a new block
        if "for" in code[-1]:
            scope = "let"
    except IndexError:
        pass

    # check if the AssignmentExpression is an Identifier
        # return a line of JavaScript code

    if expr['left']['type'] == 'MemberExpression':
        return (f"{expr['object']['name']}")

    if expr['right']['type'] == 'Identifier':
        return (f"{scope} {expr['left']['name']} = {expr['right']['value']};")
    
    # BinaryExpression
    elif expr['right']['type'] == 'BinaryExpression':
        return (f"{scope} {expr['left']['name']} = {expr['right']['left']['name']} {expr['right']['operator']} {expr['right']['right']['name']};")
    
    # ArrayExpression
    elif expr['right']['type'] == 'ArrayExpression':
        elements = []
        for i in expr['right']['elements']:
            elements.append(i['value'])
        return (f"{scope} {expr['left']['name']} = {elements};")
    
    



def ExpressionStatement(expr):
    if expr['expression']['type'] == 'CallExpression':
        return (f"console.log({expr['expression']['arguments'][0]['name']});")

def ForStatement(expr):
    code.append(f"for (let {expr['init']['name']} = 0; {expr['init']['name']} < {expr['test']['name']}.length; {expr['init']['name']}++)"+" {")
    for i in expr['body']:
        print(find_expression(i))
        code.append(find_expression(i))