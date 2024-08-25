import re

res = 0
with open("data.txt") as f:
    for line in f:
        minCount, maxCount, letter, password = re.split(r": |-| ", line)
        if int(minCount) <= password.count(letter) <= int(maxCount):
            res += 1

print(res)