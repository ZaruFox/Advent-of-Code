import itertools
def addToKnownBeacons(knownBeacons, newBeacon):
    tmp = set()
    for beacon in knownBeacons:
        knownBeacons[beacon].add((newBeacon[0]-beacon[0], newBeacon[1]-beacon[1], newBeacon[2]-beacon[2]))
        tmp.add((-newBeacon[0]+beacon[0], -newBeacon[1]+beacon[1], -newBeacon[2]+beacon[2]))
    knownBeacons[newBeacon] = tmp

def rotate(vectors):
    res = []
    for x,y,z in itertools.permutations([0,1,2]):
        res.append(set([(vector[x], vector[y], vector[z]) for vector in vectors]))
        res.append(set([(-vector[x], vector[y], vector[z]) for vector in vectors]))
        res.append(set([(vector[x], -vector[y], vector[z]) for vector in vectors]))
        res.append(set([(-vector[x], -vector[y], vector[z]) for vector in vectors]))
        res.append(set([(vector[x], vector[y], -vector[z]) for vector in vectors]))
        res.append(set([(-vector[x], vector[y], -vector[z]) for vector in vectors]))
        res.append(set([(vector[x], -vector[y], -vector[z]) for vector in vectors]))
        res.append(set([(-vector[x], -vector[y], -vector[z]) for vector in vectors]))
    return res

scanners = []

with open("data.txt") as f:
    f.readline()
    beacons = []
    
    for line in f:
        if line.startswith("---"):
            scanners.append(beacons)
            beacons = []
        elif line != "\n":
            beacons.append(tuple([int(x) for x in line.strip().split(",")]))

    scanners.append(beacons)

knownBeacons = {}
for beacon in scanners[0]:
    knownBeacons[beacon] = set()
    
    for beacon2 in scanners[0]:
        if beacon2 == beacon:
            continue
        knownBeacons[beacon].add((beacon2[0]-beacon[0], beacon2[1]-beacon[1], beacon2[2]-beacon[2]))
            
scanners = scanners[1:]
i = 0
while scanners:
    beacons = scanners[i]

    for beacon in beacons:
        distance = set()
        for beacon2 in beacons:
            distance.add((beacon2[0]-beacon[0], beacon2[1]-beacon[1], beacon2[2]-beacon[2]))

        found = False
        for type, possibleRotation in enumerate(rotate(distance)):
            for possibleMatch in knownBeacons:
                if len(knownBeacons[possibleMatch].intersection(possibleRotation)) >= 11:
                    found = True
                    break
                    
            if found:
                break
                
        if found:
            q = list(rotate([beacon])[type])[0]
            print(i, "found at", [possibleMatch[x]-q[x] for x in range(3)])
            scanners.pop(i)
            
            for vector in possibleRotation:
                foundBeacon = tuple([possibleMatch[x]+vector[x] for x in range(3)])
                if foundBeacon in knownBeacons:
                    continue

                addToKnownBeacons(knownBeacons, foundBeacon)
                
            break
            
    if not found:
        i += 1
    if i >= len(scanners):
        i = 0

print(len(knownBeacons))