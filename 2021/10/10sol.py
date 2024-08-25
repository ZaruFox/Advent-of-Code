data = []
with open("10data.txt") as f:
    for line in f:
        data.append(line.strip())

res = 0
i = 0
RELATIONS = {"<":">", "{": "}", "[":"]", "(":")"}
SCORE = {")":3, "]":57, "}":1197, ">":25137}
while i < len(data):
    stack = []
    for char in data[i]:
        if char in RELATIONS.keys():
            stack.append(RELATIONS[char])
        else:
            expected = stack.pop()
            if char != expected:
                res += SCORE[char]
                data.pop(i)
                i -= 1
                break

    i += 1

print(res)

#part 2
res = []
SCORE2 = {")":1, "]":2, "}":3, ">":4}

for chunk in data:
    stack = []
    
    for char in chunk:
        if char in RELATIONS.keys():
            stack.append(RELATIONS[char])
        else:
            stack.pop()

    currentScore = 0
    for char in stack[::-1]:
        currentScore *= 5
        currentScore += SCORE2[char]
    res.append(currentScore)

print(sorted(res)[len(res)//2])
        
        

    

    
        