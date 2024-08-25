from collections import Counter
from collections import deque
import re
import math
import sys
import heapq
from copy import deepcopy 
sys.setrecursionlimit(5000) 

def tranposed(arr):
    row,col = len(arr) , len(arr[0])
    tranposed = [[0 for x in range(row)] for y in range(col)]
    
    for r in range(row):
        for c in range(col):
            tranposed[c][r] = arr[r][c]
    return tranposed

class Factory:
    def __init__(self):
        self.workflows: dict[str,Workflow_for_parts] = {}

    def check_part(self,part, workflow_name):
        if workflow_name == 'R':
            return 0
        if workflow_name == 'A':
            return sum(part.values())
        workflow = self.workflows[workflow_name]
        for test in workflow.tests:
            criteria, passed_destination = test
            attribute_being_tested = str(criteria[0])
            attribute_value = str(part[attribute_being_tested])
            if eval (attribute_value + criteria[1::]):
                return self.check_part(part,passed_destination)
        return self.check_part(part,workflow.next_workflow)
    
class Workflow:
    def __init__(self,name = None, next_workflow = None):
        self.name = name
        self.next_workflow = next_workflow
        
class Workflow_for_parts(Workflow):
    def __init__(self,name = None, next_workflow = None):
        super().__init__(name, next_workflow)
        self.tests = [] # each element is (rule,where it goes after passing)
    def __repr__(self):
        return str(self.tests)
    
    @classmethod
    def Create_Workflow(cls,rule):
        rule = re.split("{|}|,",rule)[0:-1]
        new_workflow = cls()
        new_workflow.name = rule [0]
        new_workflow.next_workflow = rule[-1]
        for test in range(1, len(rule) -1):
            condition, result = rule[test].split(":")
            new_workflow.tests.append( (condition, result) )
        return new_workflow

def part_one(file_name):
    rules = []
    parts = []
    switch = False
    with open(file_name) as file:
        for row in file:
            if switch:
                obj = re.split("{|}|=|,",row.strip())[1:-1]
                part = { obj[i]: int(obj[i+1]) for i in range(0,8,2)}
                parts.append(part)
            elif row == "\n":
                switch = True
            else:
                rules.append(row.strip())

    factory = Factory()
    for rule in rules:
        workflow = Workflow_for_parts.Create_Workflow(rule)
        factory.workflows[workflow.name] = workflow

    res = 0
    for part in parts:
        res += factory.check_part(part,"in")
    return res


def part_two(file_name):
    rules = []
    parts = []
    switch = False
    with open(file_name) as file:
        for row in file:
            if switch:
                obj = re.split("{|}|=|,",row.strip())[1:-1]
                part = { obj[i]: int(obj[i+1]) for i in range(0,8,2)}
                parts.append(part)
            elif row == "\n":
                switch = True
            else:
                rules.append(row.strip())

    factory = Factory()
    for rule in rules:
        workflow = Workflow_for_parts.Create_Workflow(rule)
        factory.workflows[workflow.name] = workflow

    def dfs(workflow_name,domain):
        if workflow_name == "A":
            res = 1
            for key,value in domain.items():
                res *= (value[1] - value[0]+1)
            return res
        elif workflow_name == 'R':
            return 0
        res = 0
        workflow = factory.workflows[workflow_name]
        for rule in workflow.tests:
            
            criteria, passed_destination = rule
            attribute = criteria[0]
            attribute_interval = domain[attribute]
            sign = criteria[1]
            value = int(criteria[2::])
        
            d = {x:y for x,y in domain.items()}
            if sign == "<":
                passed_interval = [0,value-1]
                failed_interval = [value,4000]
            else:
                passed_interval = [value+1, 4000]
                failed_interval = [0,value]
            
            #check in boundary
            if max(passed_interval[0], attribute_interval[0]) <= min(passed_interval[1], attribute_interval[1]):
            #passed criteria
                new_interval = [ max(passed_interval[0], attribute_interval[0]) , min(passed_interval[1], attribute_interval[1]) ]
                d[attribute] = new_interval
                res += dfs(passed_destination,d)
            # else:
            #     continue
            if max(failed_interval[0], attribute_interval[0]) <= min(failed_interval[1], attribute_interval[1]):
                new_interval = [ max(failed_interval[0], attribute_interval[0]) , min(failed_interval[1], attribute_interval[1]) ]
                domain[attribute] = new_interval
        res += dfs(workflow.next_workflow, domain)
        return res
        
    return dfs('in', {'x': [1,4000], 'm': [1,4000], 'a':[1,4000], 's':[1,4000]})

if __name__ == "__main__":
    print(part_two('data.txt'))