with open("data.txt") as f:
    cups = [int(x) for x in f.readline().strip()]

currentCupI = 0

for _ in range(100):
    cupsPickedUp = []
    for i in range(3):
        cupsPickedUp.append(cups.pop(currentCupI+1))

    destinationCup = cups[currentCupI]-1
    destinationCup = (destinationCup-1) % 9 + 1
    while destinationCup in cupsPickedUp:
        destinationCup -= 1
        destinationCup = (destinationCup-1) % 9 + 1

    destinationCupI = cups.index(destinationCup)
    cups = cups[:destinationCupI+1] + cupsPickedUp + cups[destinationCupI+1:]

    cups.append(cups.pop(0))

print(cups)
    