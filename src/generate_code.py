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

    
    #get_variables(tree)
    for key in tree:
        for expr in tree[key]:
            print(expr)
            print()
            if type(expr) == str:
                pass
            elif expr['type'] == 'AssignmentExpression':
                AssignmentExpression(expr)
            elif expr['type'] == 'ExpressionStatement':
                ExpressionStatement(expr)

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

def AssignmentExpression(expr):
    # get names and values of each variable
    #js["variables"]["names"].append(expr['left']['name'])
    code.append(f"var {expr['left']['name']};")
    if expr['right']['type'] == 'Identifier':
        #js["variables"]["values"].append(expr['right']['value'])
        code.append(f"{expr['left']['name']} = {expr['right']['value']};")
    elif expr['right']['type'] == 'BinaryExpression':
        #js["variables"]["values"].append(f"{expr['right']['left']['name']} {expr['right']['operator']} {expr['right']['right']['name']}")
        code.append(f"{expr['left']['name']} = {expr['right']['left']['name']} {expr['right']['operator']} {expr['right']['right']['name']};")

def ExpressionStatement(expr):
    if expr['expression']['type'] == 'CallExpression':
        code.append(f"console.log({expr['expression']['arguments'][0]['name']});")