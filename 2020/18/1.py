def calc(equation, i):
    if equation[i] != "(":
        res = equation[i]
        i += 1
    else:
        res, i = calc(equation, i+1)
    
    while i < len(equation):
        if equation[i] == ")":
            return res, i+1

        if equation[i+1] == "(":
            val, nexti = calc(equation, i+2)
        else:
            val, nexti = equation[i+1], i+2

        if equation[i] == "+":
            res += val
        elif equation[i] == "*":
            res *= val
        else:
            raise f"Unexpected operator {equation[i]}"

        i = nexti

    return res, i


equations = []
with open("data.txt") as f:
    for line in f:
        line = line.replace("(", " ( ").replace(")", " ) ").strip()
        equation = []
        for val in line.split():
            if val.isdigit():
                equation.append(int(val))
            else:
                equation.append(val)

        equations.append(equation)

res = 0
for equation in equations:
    res += calc(equation, 0)[0]
print(res)