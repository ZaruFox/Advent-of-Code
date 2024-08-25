PREAMBLELENGTH = 25
numbers = []
target = 0

with open("data.txt") as f:
    for line in f:
        numbers.append(int(line.strip()))

for i in range(PREAMBLELENGTH, len(numbers)):
    valid = False
    hashset = set()

    for j in range(i-PREAMBLELENGTH, i):
        if numbers[j] in hashset:
            valid = True
            break
        else:
            hashset.add(abs(numbers[i] - numbers[j]))

    if not valid:
        target = numbers[i]
        break

prefixSum = [0, numbers[0]]
for i in range(1, len(numbers)):
    prefixSum.append(prefixSum[-1] + numbers[i])

hashmap = {}
for i in range(len(prefixSum)):
    if prefixSum[i] in hashmap:
        tmp = numbers[hashmap[prefixSum[i]]-1:i]
        print(max(tmp) + min(tmp))
        break
    else:
        hashmap[target+prefixSum[i]] = i