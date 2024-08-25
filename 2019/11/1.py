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
    def runIntcode(self, inputList):
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

# ====================== MAIN =======================
with open("data.txt") as f:
    intcode = [int(x) for x in f.readline().strip().split(",")]

DIRECTIONS = [(0,-1), (1,0), (0,1), (-1,0)]

robot = Complier(intcode)
curPosition = [0, 0]
direction = 0
painted = set()
paintedWhite = set()

while robot.exitCode == 1:
    colour, rotation = robot.runIntcode([1 if tuple(curPosition) in paintedWhite else 0])

    painted.add(tuple(curPosition))
    if colour == 0:
        paintedWhite.discard(tuple(curPosition))
    else:
        paintedWhite.add(tuple(curPosition))

    if rotation == 0:
        direction -= 1
    else:
        direction += 1
    direction %= 4

    curPosition[0] += DIRECTIONS[direction][0]
    curPosition[1] += DIRECTIONS[direction][1]
print(len(painted))