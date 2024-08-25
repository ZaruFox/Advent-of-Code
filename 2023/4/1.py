import re

res = 0
with open("data.txt") as f:
    for line in f:
        _, winning, numbers = [re.split("  | ", x.strip()) for x in re.split(r": | \| ", line.strip())]
        
        numberOfWins = 0
        for number in numbers:
            if number in winning:
                numberOfWins += 1

        if numberOfWins != 0:
            res += 2 ** (numberOfWins - 1)

print(res)