class Workflow:
    def __init__(self, data):
        self.operations = [x.split(":") for x in data.split(",")]
     

    def work(self, gear):
        for operation in self.operations:
            if len(operation) == 1:
                return operation[0]

            if eval(f"gear[\"{operation[0][0]}\"]{operation[0][1:]}"):
                return operation[1]

        raise Exception("Work not finished")

workflowDict = {}
objectList = []
with open("data.txt") as f:
    for line in f:
        if line == "\n":
            break
            
        name, operation = line.strip().split("{")
        workflowDict[name] = Workflow(operation[:-1])

    for line in f:
        object = line.replace("=", "\":").replace(",", ",\"").replace("{", "{\"")
        exec(f"objectList.append({object})")
        
res = 0

for object in objectList:
    currentWorkflow = "in"
    while True:
        currentWorkflow = workflowDict[currentWorkflow].work(object)
    
        if currentWorkflow == "A":
            res += sum(object.values())
            break

        if currentWorkflow == "R":
            break

print(res)      
            