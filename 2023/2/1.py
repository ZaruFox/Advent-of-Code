import re

LIMITS = {"red": 12, "green": 13, "blue": 14}
result = 0

games = []
with open("data.txt") as f:
    for line in f:
        games.append(re.split(r'; |, |: ', line.strip())[1:])

for i in range(len(games)):
    valid = True
    for reveal in games[i]:
        count, colour = reveal.split(" ")
        
        if int(count) > LIMITS[colour]:
            valid = False
            break

    if valid:
        result += i + 1

print(result)
            
        