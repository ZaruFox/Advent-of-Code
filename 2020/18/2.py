import math

def calc(equation, i):
    baseEquation = []
    if equation[i] != "(":
        baseEquation.append(equation[i])
        i += 1
    else:
        tmp, i = calc(equation, i+1)
        baseEquation.append(tmp)

    while i < len(equation):
        if equation[i] == ")":
            break

        if equation[i+1] == "(":
            val, nexti = calc(equation, i+2)
        else:
            val, nexti = equation[i+1], i+2

        if equation[i] == "+":
            baseEquation.append("+")

        baseEquation.append(val)

        i = nexti

    j = 0
    while j < len(baseEquation):
        if baseEquation[j] == "+":
            val1 = baseEquation.pop(j+1)
            val2 = baseEquation.pop(j-1)
            baseEquation[j-1] = val1+val2
        else:
            j += 1

        
    return math.prod(baseEquation), i+1


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