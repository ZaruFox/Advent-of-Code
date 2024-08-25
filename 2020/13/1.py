import math

with open("data.txt") as f:
    departureTime = int(f.readline())
    buses = [int(x) for x in f.readline().strip().split(",") if x != "x"]

minTime = math.inf
busID = 0
for loopTime in buses:
    timeWaited = loopTime * ((departureTime//loopTime) + 1) - departureTime
    if timeWaited < minTime:
        busID = loopTime
        minTime = timeWaited

print(busID * minTime)