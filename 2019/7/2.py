# for creating intcode scripts that can continuously take inputs
class Complier:
    def __init__(self, intcode):
        self.PARAMETERMODES = {0: self.positionMode, 1: self.immediateMode}
        self.OPCODES = {99: (-1, -1), 1: (self.addition, 3), 2: (self.multiplication, 3), 3: (self.saveInput, 1), 4: (self.output, 1), 5: (self.jumpIfTrue, 2), 6: (self.jumpIfFalse, 2), 7: (self.lessThan, 3), 8: (self.equalTo, 3)}
        
        self.intcode = intcode.copy()
        self.i = 0
        self.exitCode = None

   # ================ PARAMETER MODES ================

    def positionMode(self, val):
        return self.intcode[val]

    def immediateMode(self, val):
        return val

    # ================ OPERATIONS ====================

    def addition(self, arguments, converted):
        _, _, desti = arguments
        loc1, loc2, _ = converted

        self.intcode[desti] = loc1 + loc2

    def multiplication(self, arguments, converted):
        _, _, desti = arguments
        loc1, loc2, _ = converted

        self.intcode[desti] = loc1 * loc2

    def saveInput(self, desti, inputVal):
        self.intcode[desti] = inputVal

    def output(self, arguments, converted):
        return converted[0]

    def jumpIfTrue(self, arguments, converted):
        if converted[0]:
            return converted[1]

    def jumpIfFalse(self, arguments, converted):
        if not converted[0]:
            return converted[1]

    def lessThan(self, arguments, converted):
        _, _, desti = arguments
        num1, num2, _ = converted

        self.intcode[desti] = int(num1 < num2)

    def equalTo(self, arguments, converted):
        _, _, desti = arguments
        num1, num2, _ = converted

        self.intcode[desti] = int(num1 == num2)
        
    # ================ DRIVER ========================

    # program will stop if input value runs out
    # current state of intcode and pointer will be returned if returnStatus is True
    def runIntcode(self, inputList):
        outputList = []

        while self.i < len(self.intcode):
            opcode = self.intcode[self.i] % 100
            operation, argumentCount = self.OPCODES[opcode]

            # finds parameter modes of the parameters
            modes = str(self.intcode[self.i])
            modes = modes.zfill(argumentCount+2)[:-2]
            modes = [int(x) for x in modes][::-1]
            args = self.intcode[self.i+1:self.i+1+argumentCount]
            converted = self.convertArgs(modes, args)

            # handle exit
            if opcode == 99:
                self.exitCode = 0
                break

            # handle input
            elif opcode == 3:
                if not inputList:
                    self.exitCode = 1
                    break
                self.saveInput(self.intcode[self.i+1], inputList.pop(0))
                self.i += 2
                continue

            # handles output
            elif opcode == 4:
                outputList.append(self.output(self.intcode[self.i+1], converted))
                self.i += 2
                continue

            # runs the operation
            newI = operation(args, converted)

            # set i to new value if operation returns it 
            if newI:
                self.i = newI
            else:
                self.i += 1 + argumentCount

        return outputList

    # convert each arg according to the provided mode
    def convertArgs(self, modes, arguments):
        res = []
        for j in range(len(arguments)):
            res.append(self.PARAMETERMODES[modes[j]](arguments[j]))
        return res

# ====================== MAIN =======================
import itertools

with open("data.txt") as f:
    intcode = [int(x) for x in f.readline().strip().split(",")]

res = 0
for phaseSettings in itertools.permutations([5,6,7,8,9]):
    amplifiers = [Complier(intcode) for _ in range(5)]

    for i, phase in enumerate(phaseSettings):
        amplifiers[i].runIntcode([phase])
        assert amplifiers[i].exitCode == 1

    amp = 0
    while amplifiers[-1].exitCode == 1:
        for i in range(5):
            amp = amplifiers[i].runIntcode([amp])[0]

    res = max(res, amp)

print(res)