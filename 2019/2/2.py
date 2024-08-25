def addition(intcode, loc1, loc2, desti):
    intcode[desti] = intcode[loc1] + intcode[loc2]

def multiplication(intcode, loc1, loc2, desti):
    intcode[desti] = intcode[loc1] * intcode[loc2]

# ============== OPERATIONS END ====================

OPCODES = {1: (addition, 3), 2: (multiplication, 3)}

def runIntcode(intcode, noun, verb):
    intcode = intcode.copy()
    intcode[1] = noun
    intcode[2] = verb

    i = 0
    while i < len(intcode):
        opcode = intcode[i]
        if opcode == 99:
            break

        operation, argumentCount = OPCODES[opcode]

        operation(intcode, *intcode[i+1:i+1+argumentCount])
        i += 1 + argumentCount

    return intcode[0]

# ====================== MAIN =======================

with open("data.txt") as f:
    intcode = [int(x) for x in f.readline().strip().split(",")]

for noun in range(100): 
    for verb in range(100):
        if runIntcode(intcode, noun, verb) == 19690720:
            print(noun*100+verb)

