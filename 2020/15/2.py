with open("data.txt") as f:
    startingNumbers = [int(x) for x in f.readline().strip().split(",")]

hashmap = {x:i for i, x in enumerate(startingNumbers)}

i = len(startingNumbers) + 1
prevNumber = 0
while i != 30000000:
    if i % 1000000 == 0:
        print(f"{i//300000}% done")
        
    cur = i-1-hashmap[prevNumber] if prevNumber in hashmap else 0
    hashmap[prevNumber] = i-1

    prevNumber = cur
    i += 1

print(prevNumber)