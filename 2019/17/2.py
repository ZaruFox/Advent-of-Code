from collections import defaultdict

# for creating intcode scripts that can continuously take inputs
class Complier:
    def __init__(self, intcode, pointer=0, relativeBase=0):
        self.READMODES = {0: self.positionMode, 1: self.immediateMode, 2: self.relativeMode}
        self.WRITEMODES = {0: self.immediateMode, 1: -1, 2: self.relativeModeWrite}
        self.OPCODES = {99: (-1, -1, ()), 
            1: (self.addition, 3, (2,)), 
            2: (self.multiplication, 3, (2,)), 
            3: (self.saveInput, 1, (0,)), 
            4: (self.output, 1, ()), 
            5: (self.jumpIfTrue, 2, ()), 
            6: (self.jumpIfFalse, 2, ()), 
            7: (self.lessThan, 3, (2,)), 
            8: (self.equalTo, 3, (2,)), 
            9: (self.adjustBase, 1, ())}

        self.intcode = defaultdict(int)
        for i in range(len(intcode)):
            self.intcode[i] = intcode[i]
        self.i = pointer
        self.exitCode = 1
        self.relativeBase = relativeBase

   # ================ PARAMETER MODES ================

    def positionMode(self, val):
        return self.intcode[val]

    def immediateMode(self, val):
        return val

    def relativeMode(self, val):
        return self.intcode[val + self.relativeBase]

    def relativeModeWrite(self, val):
        return val + self.relativeBase

    # ================ OPERATIONS ====================

    def addition(self, args):
        self.intcode[args[2]] = args[1] + args[0]

    def multiplication(self, args):
        self.intcode[args[2]] = args[1] * args[0]

    def saveInput(self, args, inputVal):
        self.intcode[args[0]] = inputVal

    def output(self, args):
        return args[0]

    def jumpIfTrue(self, args):
        if args[0]:
            return args[1]

    def jumpIfFalse(self, args):
        if not args[0]:
            return args[1]

    def lessThan(self, args):
        self.intcode[args[2]] = int(args[0] < args[1])

    def equalTo(self, args):
        self.intcode[args[2]] = int(args[0] == args[1])

    def adjustBase(self, args):
        self.relativeBase += args[0]

    # ================ DRIVER ========================
    # program will stop if input value runs out
    # current state of intcode and pointer will be returned if returnStatus is True
    def sendInput(self, inputList=[]):
        assert self.exitCode == 1
        outputList = []

        while self.i < len(self.intcode):
            opcode = self.intcode[self.i] % 100
            operation, argumentCount, writeArgs = self.OPCODES[opcode]

            # finds parameter modes of the parameters
            modes = str(self.intcode[self.i])
            modes = modes.zfill(argumentCount+2)[:-2]
            modes = [int(x) for x in modes][::-1]

            # find args
            args = []
            for address in range(self.i+1,self.i+1+argumentCount):
                args.append(self.intcode[address])
            args = self.convertArgs(modes, args, writeArgs)

            # handle exit
            if opcode == 99:
                self.exitCode = 0
                break
            # handle input
            elif opcode == 3:
                if not inputList:
                    self.exitCode = 1
                    break
                self.saveInput(args, inputList.pop(0))
                newI = None
            # handles output
            elif opcode == 4:
                 outputList.append(operation(args))
                 newI = None
            else:
                newI = operation(args)

            # set i to new value if operation returns it 
            self.i = newI if newI != None else self.i + 1 + argumentCount

        return outputList

    # convert each arg according to the provided mode
    def convertArgs(self, modes, args, writeArgs):
        res = []
        for j in range(len(args)):
            if j not in writeArgs:
                res.append(self.READMODES[modes[j]](args[j]))
            else:
                res.append(self.WRITEMODES[modes[j]](args[j]))
        return res

    def copy(self):
        return Complier(self.intcode, self.i, self.relativeBase)

# ====================== MAIN =======================

def gridFromAscii(data):
    res = [[]]

    for char in data:
        if char == 10:
            res.append([])
        else:
            res[-1].append(chr(char))

    return res


with open("data.txt") as f:
    intcode = [int(x) for x in f.readline().strip().split(",")]

intcode[0] = 2
ascii = Complier(intcode)
grid = gridFromAscii(ascii.sendInput())
grid = [["."] * len(grid[0])] + grid[:-3] + [["."] * len(grid[0])]
grid = [["."]+line+["."] for line in grid]

print("\n".join(["".join(x) for x in grid]))

DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))
cur = [grid[1].index("^"), 1]
curDir = 3
res = ["L"]

while True:
    steps = 0
    while grid[cur[1] + DIRECTIONS[curDir][1]][cur[0] + DIRECTIONS[curDir][0]] == "#":
        cur[0] += DIRECTIONS[curDir][0]
        cur[1] += DIRECTIONS[curDir][1]
        steps += 1

    res.append(str(steps))

    left = grid[cur[1] + DIRECTIONS[(curDir-1)%4][1]][cur[0] + DIRECTIONS[(curDir-1)%4][0]]
    right = grid[cur[1] + DIRECTIONS[(curDir+1)%4][1]][cur[0] + DIRECTIONS[(curDir+1)%4][0]]

    if left == "#":
        res.append("L")
        curDir = (curDir-1)%4
    elif right == "#":
        res.append("R")
        curDir = (curDir+1)%4
    else:
        break

routines = [["A", "B", "A", "C", "B", "A", "B", "C", "C", "B"], ['L', '12', 'L', '12', 'R', '4'], ['R', '10', 'R', '6', 'R', '4', 'R', '4'], ['R', '6', 'L', '12', 'L', '12']]
routines = [[ord(x) for x in ",".join(routine)] + [10] for routine in routines]

for routine in routines:
    ascii.sendInput(routine)

print(ascii.sendInput([ord("n"), 10]))

