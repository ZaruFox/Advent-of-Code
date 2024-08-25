import re

res = 0
with open("data.txt") as f:
    for line in f:
        i1, i2, letter, password = re.split(r": |-| ", line)
        if (password[int(i1)-1] == letter) != (password[int(i2)-1] == letter):
            res += 1

print(res)