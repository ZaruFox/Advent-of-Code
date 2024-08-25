with open("data.txt") as f:
    numberOfRecipies = int(f.readline())

recipes = [3, 7]
i, j = 0, 1

while len(recipes) < numberOfRecipies + 10:
    score = recipes[i] + recipes[j]

    recipes.extend([int(x) for x in str(score)])

    i += 1 + recipes[i]
    i %= len(recipes)
    j += 1 + recipes[j]
    j %= len(recipes)

print(*recipes[numberOfRecipies: numberOfRecipies+10], sep="")