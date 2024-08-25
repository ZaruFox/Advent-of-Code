with open("data.txt") as f:
    times = [int(x) for x in f.readline().strip().split()[1:]]
    records = [int(x) for x in f.readline().strip().split()[1:]]

res = 1
for i in range(len(times)):
    totalTime = times[i]
    record = records[i]
    numberOfWays = 0

    for timePressed in range(totalTime):
        if timePressed*(totalTime-timePressed) > record:
            numberOfWays += 1

    res *= numberOfWays


print(res)