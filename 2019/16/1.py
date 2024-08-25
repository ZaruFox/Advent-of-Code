import itertools

with open("data.txt") as f:
    numbers = [int(x) for x in f.readline().strip()]

PATTERN = [1, 0, -1, 0]

for __ in range(100):
    newNumbers = []
    for i in range(len(numbers)):
        new = 0
        j = i
    
        for factor in itertools.cycle(PATTERN):
            if j+i+1 > len(numbers):
                new += sum(numbers[j:]) * factor
                break

            if factor != 0:
                new += sum(numbers[j:j+i+1]) * factor

            j += i+1
    
        newNumbers.append(abs(new) % 10)
    numbers = newNumbers
print("".join([str(x) for x in numbers[:8]]))