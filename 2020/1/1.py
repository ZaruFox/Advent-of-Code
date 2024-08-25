hashmap = {}
with open("data.txt") as f:
    for line in f:
        number = int(line)
        
        if number in hashmap:
            print(number * hashmap[number])
            break
        else:
            hashmap[2020-number] = number