import re
import math

class Workflow:
    def __init__(self, data):
        self.operations = [x.split(":") for x in data.split(",")]

workflowDict = {}
with open("data.txt") as f:
    for line in f:
        if line == "\n":
            break

        name, operation = line.strip().split("{")
        workflowDict[name] = Workflow(operation[:-1])


res = 0
def dfs(cur):
    elseOperations = []
    newPaths = []
    for operation in workflowDict[cur].operations[:-1]:
        if operation[1] == "A":
            newPaths.append([operation[0]]+elseOperations)
        elif operation[1] != "R":
            for path in dfs(operation[1]):
                newPaths.append(path + [operation[0]]+elseOperations)

        
        elseOperations.append("!" + operation[0])

    if workflowDict[cur].operations[-1][0] == "A":
        newPaths.append(elseOperations)
    elif workflowDict[cur].operations[-1][0] != "R":
        for path in dfs(workflowDict[cur].operations[-1][0]):
            newPaths.append(path + elseOperations)

    return newPaths

res = 0
validConditions = dfs("in")
for conditionList in validConditions:
    intervals = {"x": [1,4000], "m": [1,4000], "a": [1,4000], "s": [1,4000]}
    
    for condition in conditionList:
        number = int(re.split(r">|<",condition)[1])
        
        if not condition.startswith("!"):
            interval = intervals[condition[0]]
            if condition[1] == ">":
                interval[0] = max(interval[0], number + 1)
            else:
                interval[1] = min(interval[1], number - 1)
                
        else:
            interval = intervals[condition[1]]
            if condition[2] == ">":
                interval[1] = min(interval[1], number)
            else:
                interval[0] = max(interval[0], number)

    res += math.prod([max(r-l+1, 0) for l, r in intervals.values()])

print(res)