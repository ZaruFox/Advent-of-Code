"""
A=7 offset 4, B=5 offset 0, C=3 offset 1
0    5         15   20        30
v    v         v    v         v
C--C--C--C--C--C--C--C--C--C--C--C--C--C--C--C--C
A------A------A------A------A------A------A------A
B----B----B----B----B----B----B----B----B----B
^         ^                        ^         ^
T0        Ta                       Tb        Tc
0         10                       35        45

"""
with open("data.txt") as f:
    departureTime = int(f.readline())
    buses = [(i, int(x)) for i, x in enumerate(f.readline().strip().split(",")) if x != "x"]
print(buses)
res = 0
increment = buses[0][1]
for offset, loopTime in buses[1:]:
    print("Next Bus", loopTime, "Res", res, "increment", increment)
    while True:
        res += increment
        timeWaited = loopTime * ((res//loopTime) + 1) - res
        if timeWaited == offset % loopTime:
            break
    increment *= loopTime
print(res)
    

