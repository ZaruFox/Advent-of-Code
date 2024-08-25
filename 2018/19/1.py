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

OPCODES = {x.__name__: x for x in [addi, addr, muli, mulr, bani, banr, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]}

with open("data.txt") as f:
    data = f.read().splitlines()

pointerIndex = int(data[0].lstrip("#ip "))
pointerValue = 0
instructions = [x.split(" ") for x in data[1:]]
registers = [0] * 6

while registers[pointerIndex] < len(instructions):
    registers[pointerIndex] = pointerValue

    func, a, b, c = instructions[pointerValue] 

    OPCODES[func](registers, int(a), int(b), int(c))

    pointerValue = registers[pointerIndex]
    pointerValue += 1

print(registers[0])

