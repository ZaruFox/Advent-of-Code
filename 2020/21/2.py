from collections import defaultdict, Counter
ingredients = defaultdict(list)
ingredientsCount = defaultdict(int)
allergensCount = defaultdict(int)

with open("data.txt") as f:
    for line in f:
        allergens = False
        currentIngredients = []
        currentAllergens = []
        for word in line.strip(")\n").split():
            if not allergens:
                if word == "(contains":
                    allergens = True
                    continue

                currentIngredients.append(word)
                ingredientsCount[word] += 1
            else:
                currentAllergens.append(word.strip(","))
                allergensCount[word.strip(",")] += 1

        for ingredient in currentIngredients:
            ingredients[ingredient] += currentAllergens

ingredients = {x:[key for key, count in Counter(ingredients[x]).items() if count == allergensCount[key]] for x in ingredients}
ingredients = {key:set(value) for key, value in ingredients.items() if value != []}

foundAllergens = set()
while any(len(x) != 1 for x in ingredients.values()):
    for ingredient in ingredients:
        if len(ingredients[ingredient]) == 1:
            foundAllergens.add(list(ingredients[ingredient])[0])
            continue
            
        for found in foundAllergens:
            ingredients[ingredient].discard(found)

print(",".join(sorted(ingredients.keys(), key= lambda x: list(ingredients[x])[0])))

