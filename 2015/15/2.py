from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy
import z3

# Read input data
with open("data.txt") as f:
    data = [[int(x) for x in re.findall(r"-?\d+", line)] for line in f.read().splitlines()]

o = z3.Optimize()
num_ingredients = len(data)
ingredients = [z3.Int(f"x{i}") for i in range(num_ingredients)]

o.add(z3.Sum(ingredients) == 100)
for i in range(num_ingredients):
    o.add(ingredients[i] >= 0)

properties = [z3.Int(f"property_{i}") for i in range(5)]

for j in range(5):
    o.add(properties[j] == z3.Sum([ingredients[i] * data[i][j] for i in range(num_ingredients)]))

non_negative_properties = [z3.If(properties[j] > 0, properties[j], 0) for j in range(5)]

score = z3.Int("score")
o.add(score == non_negative_properties[0] *
               non_negative_properties[1] *
               non_negative_properties[2] *
               non_negative_properties[3])
o.add(non_negative_properties[4] == 500)
o.maximize(score)

if o.check() == z3.sat:
    model = o.model()
    print("Optimal Score:", model[score])
    for i in range(num_ingredients):
        print(f"Ingredient {i}: {model[ingredients[i]]}")
else:
    print("No solution found!")
