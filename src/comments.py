def comments(js_ast, textlist):
    # create list of expressions
    exprlist = []
    for key in js_ast:
        for expr in js_ast[key]:
            if type(expr) == str:
                pass
            else:
                exprlist.append(expr)
                

    # add commented lines to list of expressions
    for i in range(len(textlist)):
        if "#" in textlist[i]:
            if i != 0:
                exprlist.insert(i, {
                    "type": "Comment",
                    "value": textlist[i].replace("#","")
                })
            else:
                exprlist.insert(0, {
                    "type": "Comment",
                    "value": textlist[i].replace("#","")
                })
    return exprlist