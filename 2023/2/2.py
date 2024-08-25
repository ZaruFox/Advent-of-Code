import re
import math

result = 0
games = []
with open("data.txt") as f:
    for line in f:
        games.append(re.split(r"; |, |: ", line.strip())[1:])

for i in range(len(games)):
    maximum = {"red": 0, "green": 0, "blue": 0}
    
    for reveal in games[i]:
        count, colour = reveal.split(" ")
        maximum[colour] = max(maximum[colour], int(count))

    result += math.prod(maximum.values())
    
print(result)

