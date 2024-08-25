data = []
with open("data.txt") as f:
    for line in f:
        data.append([int(x) for x in line.strip().split()])

def extrapolate(row):
    if len(set(row)) == 1:
        return row[0]
    return row[-1] + extrapolate([row[i]-row[i-1] for i in range(1, len(row))])

print(sum([extrapolate(row) for row in data]))