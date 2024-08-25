chain = []
instructions = {}

with open("14data.txt") as f:
    chain = list(f.readline().strip())
    f.readline()
    for line in f:
        temp = line.strip().split(" -> ")
        instructions[temp[0]] = temp[1]


for _ in range(10):
    i = 0
    while i < len(chain)-1:
        try:
            insertValue = instructions[chain[i] + chain[i+1]]
            chain.insert(i+1, insertValue)
            i += 2
        except KeyError:
            i += 1

max_ = 0
min_ = 9999999999999
for letter in set(chain):
    max_ = max(max_, chain.count(letter))
    min_ = min(min_, chain.count(letter))

print(max_-min_)

#part 2
chain = []
instructions = {}

with open("14data.txt") as f:
    chain = list(f.readline().strip())
    f.readline()
    for line in f:
        temp = line.strip().split(" -> ")
        instructions[temp[0]] = temp[1]

pairs = {}
for i in range(len(chain)-1):
    try:
        pairs[chain[i] + chain[i+1]] += 1
    except KeyError:
        pairs[chain[i] + chain[i+1]] = 1


for _ in range(40):
    newPairs = {}
    for key, value in pairs.items():
        if key in instructions.keys():
            try:
                newPairs[key[0] + instructions[key]] += value
            except KeyError:
                newPairs[key[0] + instructions[key]] = value
    
            try:
                newPairs[instructions[key] + key[1]] += value
            except KeyError:
                newPairs[instructions[key] + key[1]] = value
            
        pairs = newPairs

countLetters = {}

for key, value in pairs.items():
    try:
        countLetters[key[0]] += value
    except KeyError:
        countLetters[key[0]] = value

    try:
        countLetters[key[1]] += value
    except KeyError:
        countLetters[key[1]] = value

countLetters[chain[0]] += 1
countLetters[chain[-1]] += 1

max_ = 0
min_ = 9999999999999
for val in countLetters.values():
    max_ = max(max_, val/2)
    min_ = min(min_, val/2)

print((max_-min_))


