from itertools import product

operations = ["and", "or", "!=", "<=", "=="]

expr = input()
expr = expr.replace("->", "<=").replace("~", "==")
expr = expr.replace("^", "!=")
expr2 = list(expr)
expr = expr.replace("(", "( ").replace(")", " )").split()
pere = []
alph = [chr(i).upper() for i in range(97, 123)]
for a in alph:
    if a in expr:
        pere.append(a)
print(*pere, "F")
for elem in product("01", repeat=len(pere)):
    for i in range(len(pere)):
        exec(f"{pere[i]} = {elem[i]}")
    f = "".join(expr2.copy())
    while "(" in f:
        flag = False
        skobki = ""
        skobki2 = ""
        for i in range(len(f)):
            elem2 = f[i]
            if flag and elem2 == "(":
                continue
            if flag and elem2 != ")":
                skobki += elem2
                skobki2 += elem2
            elif flag and elem2 == ")":
                break
            if elem2 == "(" and "(" not in f[i + 1:]:
                flag = True
        skobki = skobki.split()
        while "not" in skobki:
            skobki = (
                skobki[: skobki.index("not")]
                + [int(eval(f'not {skobki[skobki.index("not") + 1]}'))]
                + skobki[skobki.index("not") + 2:]
            )
        for operation in operations:
            while operation in skobki:
                skobki = (
                    skobki[: skobki.index(operation) - 1]
                    + [
                        int(
                            eval(
                                f"{skobki[skobki.index(operation) - 1]} "
                                f"{operation} {skobki[skobki.index(operation) + 1]}"
                            )
                        )
                    ]
                    + skobki[skobki.index(operation) + 2:]
                )
        f = (
            f[: f.find(skobki2) - 1]
            + str(skobki[0])
            + f[f.find(skobki2) + len(skobki2) + 1:]
        )

    while "not" in f:
        f = (
            f[: f.find("not")]
            + str(int(eval(f'not {f[f.find("not") + 4]}')))
            + f[f.find("not") + 5:]
        )

    for operation in operations:
        while operation in f:
            z = 0
            if operation == "and":
                z = 1
            f = "{0}{1}{2}".format(
                f[: f.find(operation) - 2],
                str(
                    int(
                        eval(
                            f"{f[f.find(operation) - 2]} {operation} {f[f.find(operation) + 3 + z]}"
                        )
                    )
                ),
                f[f.find(operation) + 4 + z:],
            )

    print(*elem, f)
