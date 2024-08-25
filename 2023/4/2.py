import re

winningCard = []
numberCard = []
with open("data.txt") as f:
    for line in f:
        _, winning, numbers = [re.split("  | ", x.strip()) for x in re.split(r": | \| ", line.strip())]
        winningCard.append(winning)
        numberCard.append(numbers)

countOfCards = [1] * len(winningCard)
for i in range(len(winningCard)):
    numberOfWins = 0
    for number in numberCard[i]:
        if number in winningCard[i]:
            numberOfWins += 1

    for j in range(i+1, i+numberOfWins+1):
       countOfCards[j] += countOfCards[i]
        
print(sum(countOfCards))