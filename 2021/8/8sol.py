data = []
with open("8data.txt") as f:
    for line in f:
        data.append([x.split(" ") for x in line.strip().split(" | ")])

res = 0
for code in [x[1] for x in data]:
    for num in code:
        if len(num) in (2,4,3,7):
            res += 1

print(res)

#part 2
res = 0
LENGTHTONUM = {2: 1, 4: 4, 3: 7, 7: 8}
NUMTOSEGMENTS = {0: (1, 2, 3, 5, 6, 7), 1: (3,6), 2: (1,3,4,5,7), 3:(1,3,4,6,7), 4:(2,3,4,6), 5:(1,2,4,6,7), 6:(1,2,4,5,6,7), 7:(1,3,6), 8:(1,2,3,4,5,6,7), 9:(1,2,3,4,6,7)}

for info in data:
    segToLetter = {}
    numToIndex = {}

    for i in range(len(info[0])):
        if len(info[0][i]) in (2,4,3,7):
            numToIndex[LENGTHTONUM[len(info[0][i])]] = i

    #decoding manually because fuck
    digitsCodes = [set(x) for x in info[0]]

    #find seg 1
    segToLetter[1] = list(digitsCodes[numToIndex[7]] - digitsCodes[numToIndex[1]])[0]

    #find seg 3,6 and index of No.6
    for i, x in enumerate(digitsCodes):
        if len(x) == 6 and list(digitsCodes[numToIndex[8]]-x)[0] in digitsCodes[numToIndex[1]]:
            segToLetter[3] = list(digitsCodes[numToIndex[8]]-x)[0]
            segToLetter[6] = list(digitsCodes[numToIndex[1]]-{segToLetter[3]})[0]
            numToIndex[6] = i
    
    #find index of No.0, No.9, No.5, No.2, No.3
    check = digitsCodes[numToIndex[4]] - digitsCodes[numToIndex[1]]
    for i, x in enumerate(digitsCodes):
        if len(x) == 6 and len(check.intersection(x)) == 1:
            numToIndex[0] = i
        elif len(x) == 6 and i != numToIndex[6]:
            numToIndex[9] = i
        elif len(x) == 5 and len(check.intersection(x)) == 2:
            numToIndex[5] = i
        elif len(x) == 5 and len(check.intersection(x)) == 1:
            if segToLetter[6] in x:
                numToIndex[3] = i
            else:
                numToIndex[2] = i

    resMinor = ""
    for resCode in info[1]:
        for i in range(10):
            if set(info[0][numToIndex[i]]) == set(resCode):
                resMinor += str(i)

    res += int(resMinor)
    
print(res)
    
            
    
