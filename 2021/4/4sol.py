order = []
boards = []
winningBoard = None

with open("4data.txt") as f:
    order = f.readline().strip().split(",")

    for line in f:
       if line == "\n":
           boards.append([])
           for _ in range(5):
               boards[-1].append([x for x in f.readline().strip().split(" ") if x != ""])


for chosenNum in order:
    # wtf
    for boardIndex, board in enumerate(boards):
        for row in board:
            for num in range(len(row)):
                if row[num] == chosenNum:
                    row[num] = None

                    if len(set(row)) == 1:
                        winningBoard = boardIndex

                    allNone = True
                    for row in board:
                        if row[num] != None:
                            allNone = False

                    if allNone:
                        winningBoard = boardIndex

    if winningBoard != None:
        total = 0
        for row in boards[winningBoard]:
            for num in row:
                if num != None:
                    total += int(num)

        print(total * int(chosenNum))
        break

#part 2
order = []
boards = []

with open("4data.txt") as f:
    order = f.readline().strip().split(",")

    for line in f:
       if line == "\n":
           boards.append([])
           for _ in range(5):
               boards[-1].append([x for x in f.readline().strip().split(" ") if x != ""])
               
oriBoards = boards.copy()
prev = None
for chosenNum in order:
    # wtf
    for boardIndex, board in enumerate(boards):
        if board == None:
            continue
            
        for row in board:
            for num in range(len(row)):
                if row[num] == chosenNum:
                    row[num] = None

                    if len(set(row)) == 1:
                        prev = board
                        boards[boardIndex] = None
                        break

                    allNone = True
                    for row in board:
                        if row[num] != None:
                            allNone = False

                    if allNone:
                        prev = board
                        boards[boardIndex]  = None

    if len([x for x in boards if x != None]) == 0:
        total = 0
        for row in prev:
            for num in row:
                if num != None:
                    total += int(num)

        print(total * int(chosenNum))
        break
