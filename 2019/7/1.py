def positionMode(intcode, val):
    return intcode[val]

def immediateMode(intcode, val):
    return val

PARAMETERMODES = {0: positionMode, 1: immediateMode}

# =============== PARAMETER MODES END ==============

def addition(intcode, arguments, converted):
    _, _, desti = arguments
    loc1, loc2, _ = converted

    intcode[desti] = loc1 + loc2

def multiplication(intcode, arguments, converted):
    _, _, desti = arguments
    loc1, loc2, _ = converted

    intcode[desti] = loc1 * loc2

def saveInput(intcode, desti, inputVal):
    intcode[desti] = inputVal

def output(intcode, arguments, converted):
    return converted[0]

def jumpIfTrue(intcode, arguments, converted):
    if converted[0]:
        return converted[1]

def jumpIfFalse(intcode, arguments, converted):
    if not converted[0]:
        return converted[1]

def lessThan(intcode, arguments, converted):
    _, _, desti = arguments
    num1, num2, _ = converted

    intcode[desti] = int(num1 < num2)

def equalTo(intcode, arguments, converted):
    _, _, desti = arguments
    num1, num2, _ = converted

    intcode[desti] = int(num1 == num2)

OPCODES = {99: (-1, -1), 1: (addition, 3), 2: (multiplication, 3), 3: (saveInput, 1), 4: (output, 1), 5: (jumpIfTrue, 2), 6: (jumpIfFalse, 2), 7: (lessThan, 3), 8: (equalTo, 3)}

# ============== OPERATIONS END ====================

# convert each arg according to the provided mode
def convertArgs(intcode, modes, arguments):
    res = []
    for i in range(len(arguments)):
        res.append(PARAMETERMODES[modes[i]](intcode, arguments[i]))
    return res

# input list will be passed in order
def runIntcode(intcode, inputList):
    intcode = intcode.copy()
    outputList = []

    i = 0
    while i < len(intcode):
        opcode = intcode[i] % 100
        operation, argumentCount = OPCODES[opcode]

        # finds parameter modes of the parameters
        modes = str(intcode[i])
        modes = modes.zfill(argumentCount+2)[:-2]
        modes = [int(x) for x in modes][::-1]
        args = intcode[i+1:i+1+argumentCount]
        converted = convertArgs(intcode, modes, args)

        # handle exit
        if opcode == 99:
            break
        # handle input
        elif opcode == 3:
            saveInput(intcode, intcode[i+1], inputList.pop(0))
            i += 2
            continue
        # handles output
        elif opcode == 4:
            outputList.append(output(intcode, intcode[i+1], converted))
            i += 2
            continue

        # runs the operation
        newI = operation(intcode, args, converted)

        # set i to new value if operation returns it 
        if newI:
            i = newI
        else:
            i += 1 + argumentCount

    return outputList

# ====================== MAIN =======================
import itertools

with open("data.txt") as f:
    intcode = [int(x) for x in f.readline().strip().split(",")]

res = 0
for phaseSettings in itertools.permutations([0,1,2,3,4]):
    amp = 0
    for phase in phaseSettings:
        amp = runIntcode(intcode, [phase, amp])[0]

    res = max(res, amp)

print(res)