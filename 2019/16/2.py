import itertools
import sys


with open("data.txt") as f:
    numbers = [int(x) for x in f.readline().strip()]

resIndex = int("".join([str(x) for x in numbers[:7]]))
PATTERN = [1, 0, -1, 0]
numbers *= 10000

for step in range(100):
    newNumbers = []
    prefixSum = [0]
    for i in range(len(numbers)):
        prefixSum.append(prefixSum[-1] + numbers[i])

    for i in range(len(numbers)):
        if i % 50000 == 0:
            print("\r", step, i/len(numbers)*100)
        new = 0
        j = i
    
        for factor in itertools.cycle(PATTERN):
            if j+i+1 > len(numbers):
                if factor != 0:
                    new += (prefixSum[-1]-prefixSum[j]) * factor
                break

            if factor != 0:
                new += (prefixSum[j+i+1]-prefixSum[j])  * factor

            j += i+1
    
        newNumbers.append(abs(new) % 10)
    numbers = newNumbers

for i in range(resIndex, resIndex + 8):
    print(numbers[i], end="")