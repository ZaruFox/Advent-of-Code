def addr(regi, a, b, c):
    regi[c] = regi[a] + regi[b]

def addi(regi, a, b, c):
    regi[c] = regi[a] + b

def mulr(regi, a, b, c):
    regi[c] = regi[a] * regi[b]

def muli(regi, a, b, c):
    regi[c] = regi[a] * b

def banr(regi, a, b, c):
    regi[c] = regi[a] & regi[b]

def bani(regi, a, b, c):
    regi[c] = regi[a] & b

def borr(regi, a, b, c):
    regi[c] = regi[a] | regi[b]

def bori(regi, a, b, c):
    regi[c] = regi[a] | b

def setr(regi, a, b, c):
    regi[c] = regi[a]

def seti(regi, a, b, c):
    regi[c] = a

def gtir(regi, a, b, c):
    regi[c] = int(a > regi[b])

def gtri(regi, a, b, c):
    regi[c] = int(regi[a] > b)

def gtrr(regi, a, b, c):
    regi[c] = int(regi[a] > regi[b])

def eqir(regi, a, b, c):
    regi[c] = int(a == regi[b])

def eqri(regi, a, b, c):
    regi[c] = int(regi[a] == b)

def eqrr(regi, a, b, c):
    regi[c] = int(regi[a] == regi[b])

OPS = [addi, addr, muli, mulr, bani, banr, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
with open('data.txt') as f:
    data = f.read().splitlines()

examples = []
for i in range(0, len(data), 4):
    if data[i] == "":
        break

    examples.append((eval(data[i].lstrip("Before: ")), [int(x) for x in data[i+1].split(" ")], eval(data[i+2].lstrip("After: "))))

program = []
for j in range(i+2, len(data)):
    program.append([int(x) for x in data[j].split(" ")])

res = 0
for regiStart, command, regiEnd in examples:
    matches = 0
    for func in OPS:
        tmp = regiStart.copy()
        func(tmp, *command[1:])
        if tmp == regiEnd:
            matches += 1

    if matches > 2:
        res += 1
    
print(res)
