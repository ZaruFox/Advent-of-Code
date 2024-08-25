from collections import defaultdict

# for creating intcode scripts that can continuously take inputs
class Complier:
    def __init__(self, intcode):
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
        self.i = 0
        self.exitCode = 1
        self.relativeBase = 0

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
    def runIntcode(self, inputList=[]):
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
            self.i = newI if newI else self.i + 1 + argumentCount

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

# ==================== PRINT HELPER  ==================
import time
import re, sys

class Reprinter:
    def __init__(self):
        self.text = ''

    def moveup(self, lines):
        for _ in range(lines):
            sys.stdout.write("\x1b[A")

    def reprint(self, text):
        # Clear previous text by overwritig non-spaces with spaces
        self.moveup(self.text.count("\n"))
        sys.stdout.write(re.sub(r"[^\s]", " ", self.text))

        # Print new text
        lines = min(self.text.count("\n"), text.count("\n"))
        self.moveup(lines)
        sys.stdout.write(text)
        self.text = text

# ==================== MAIN ========================

with open("data.txt") as f:
    intcode = [int(x) for x in f.readline().strip().split(",")]

tiles = {}
def printLocations(data, printer, score):
    idToChar = {0: " ", 1: "#", 2: "+", 3: "=", 4: "O"}

    for i in range(0, len(data), 3):
        if data[i] == -1:
            score = data[i+2]
            continue
            
        tiles[(data[i], data[i+1])] = data[i+2]

    res = f"Score: {score}\n"
    xValues = [x[0] for x in tiles.keys()]
    yValues = [x[1] for x in tiles.keys()]
    for y in range(min(yValues), max(yValues)+1):
        for x in range(min(xValues), max(xValues)+1):
            if (x, y) not in tiles:
                res += " "
            else: 
                if tiles[(x, y)] == 3:
                    paddleX = x
                elif tiles[(x, y)] == 4:
                    ballX = x
                res += idToChar[tiles[(x, y)]]
            
        res += "\n"

    printer.reprint(res)
    return ballX, paddleX, score
            
intcode[0] = 2
score = 0
directionDict = {"L":-1, "R":1, "":0}
computer = Complier(intcode)
printer = Reprinter()

data = computer.runIntcode()
while computer.exitCode == 1:
    ballX, paddleX, score = printLocations(data, printer, score)

    """
    direction = input("Enter direction (L/R): ").upper()
    data = computer.runIntcode([directionDict[direction]])
    """
    if ballX < paddleX:
        direction = -1
    elif ballX > paddleX:
        direction = 1
    else:
        direction = 0

    data = computer.runIntcode([direction])
    time.sleep(0.05)
printLocations(data, printer, score)
print(score)