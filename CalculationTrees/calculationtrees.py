def construct_forest(function_defs):
    def parse_function_def(function_def):
        parts = function_def.split("=")
        function = parts[0].strip().split("(")[0].strip()
        expression = parts[1].strip()
        tree = [function]
        if "+" in expression or "-" in expression or "*" in expression or "^" in expression:
            operator = "+" if "+" in expression else "-" if "-" in expression else "*" if "*" in expression else "^"
            parts = expression.split(operator)
            tree.append(operator)
            tree.append(parse_term(parts[0].strip()))
            tree.append(parse_term(parts[1].strip()))
        else:
            tree.append("")
            tree.append(parse_term(expression))
            tree.append([])
        return tree
        

    def parse_term(term):
        if "(" in term:
            function = term.split("(")[0].strip()
            return [function]
        elif term == "x":
            return ["x"]
        else:
            return [term]

    forest = []
    for function_def in function_defs:
        tree = parse_function_def(function_def)
        if tree[0] not in [t[0] for t in forest]:
            forest.append(tree)
    my_dict = {}
    for i in forest:
        my_dict[i[0]] = i[1:]
    def recursive_check(L):
        for i in range(len(L[2:])):
            if L[2:][i][0].isdigit() or L[2:][i][0] == "x":
                continue
            else:
                new_list = my_dict[L[2:][i][0]]
                L[2:][i] += new_list
    for eleman in forest:
        recursive_check(eleman)
    output = []
    for i, v in enumerate(forest):
        is_matched = False
        for j, w in enumerate(forest):
            if i != j and v in w:
                is_matched = True
                break
        if not is_matched:
            output.append(v)
    return output





