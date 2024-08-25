from collections import defaultdict

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
opcodes = [set(range(len(OPS))) for x in range(len(OPS))]
for regiStart, command, regiEnd in examples:
    matches = set()
    for i, func in enumerate(OPS):
        tmp = regiStart.copy()
        func(tmp, *command[1:])
        if tmp == regiEnd:
            matches.add(i)

    opcodes[command[0]] &= matches

while any(len(x) != 1 for x in opcodes):
    for i in range(len(opcodes)):
        candidates = opcodes[i]
        if len(candidates) == 1:
            num = list(candidates)[0]

            for j in range(len(opcodes)):
                if i == j:
                    continue

                opcodes[j].discard(num)

opcodes = [OPS[x.pop()] for x in opcodes]

registers = [0, 0, 0, 0]
for command in program:
    opcodes[command[0]](registers, *command[1:])

print(registers[0])