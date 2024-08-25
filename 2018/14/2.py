with open("data.txt") as f:
    recipeNeeded = f.readline()
    recipeNeeded = [int(x) for x in recipeNeeded]

recipes = [3, 7]
found = False
i, j = 0, 1

while not found:
    score = recipes[i] + recipes[j]

    for nextRecipe in str(score):
        recipes.append(int(nextRecipe))

        if recipes[-len(recipeNeeded):len(recipes)] == recipeNeeded:
            print(len(recipes) - len(recipeNeeded))
            found = True
            break

    i += 1 + recipes[i]
    i %= len(recipes)
    j += 1 + recipes[j]
    j %= len(recipes)

