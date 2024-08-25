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
    desti = converted[0]
    
    print(desti)

OPCODES = {1: (addition, 3), 2: (multiplication, 3), 3: (saveInput, 1), 4: (output, 1)}

# ============== OPERATIONS END ====================

def convertArgs(intcode, modes, arguments):
    res = []
    for i in range(len(arguments)):
        res.append(PARAMETERMODES[modes[i]](intcode, arguments[i]))
    return res

def runIntcode(intcode, programInput):
    intcode = intcode.copy()

    i = 0
    while i < len(intcode):
        opcode = intcode[i] % 100

        # handle exit
        if opcode == 99:
            break
        # handle input
        elif opcode == 3:
            saveInput(intcode, intcode[i+1], programInput)
            i += 2
            continue

        operation, argumentCount = OPCODES[opcode]

        # finds parameter modes of the parameters
        modes = str(intcode[i]).zfill(argumentCount+2)[:-2]
        modes = [int(x) for x in modes][::-1]

        args = intcode[i+1:i+1+argumentCount]
        
        operation(intcode, args, convertArgs(intcode, modes, args))
        
        i += 1 + argumentCount

    return intcode[0]

# ====================== MAIN =======================

with open("data.txt") as f:
    intcode = [int(x) for x in f.readline().strip().split(",")]

runIntcode(intcode, 1)