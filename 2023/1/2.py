import regex as re

NUMBERS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
res = 0
with open("data.txt") as f:
    for line in f:
        matches = re.findall(rf"\d|{'|'.join(NUMBERS.keys())}", line, overlapped=True)
        res += (int(matches[0]) if matches[0].isdigit() else NUMBERS[matches[0]]) * 10
        res += (int(matches[-1]) if matches[-1].isdigit() else NUMBERS[matches[-1]])
print(res)

