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
        AssignmentExpression(expr)
    elif expr['type'] == 'ExpressionStatement':
        ExpressionStatement(expr)
    elif expr['type'] == 'ForStatement':
        ForStatement(expr)

def AssignmentExpression(expr):
    # Variable to control scoping. Default is function-scoped
    scope = "var"
    left = ""
    right = ""
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
        left = (f"\t{expr['left']['object']['name']}[{expr['left']['property']['name']}]")
        if expr['right']['type'] == 'BinaryExpression':
            operator = expr['right']['operator']
            right = (f"{expr['right']['left']['object']['name']}[{expr['left']['property']['name']}] {operator} {expr['right']['right']['value']};")
            operator = expr['operator']
            code.append(f"{left} {operator} {right}")
            return


    elif expr['left']['type'] == 'Identifier':
        left = (f"{scope} {expr['left']['name']}")


    if expr['right']['type'] == 'Identifier':
        right = (f"{expr['right']['value']};")
    
    # BinaryExpression
    elif expr['right']['type'] == 'BinaryExpression':
        operator = expr['right']['operator']
        right = (f"{expr['right']['left']['name']} {operator} {expr['right']['right']['name']};")
    
    # ArrayExpression
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