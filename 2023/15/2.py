def hash(word):
    cur = 0

    for chara in word:
        cur += ord(chara)
        cur *= 17
        cur %= 256

    return cur


with open("data.txt") as f:
    data = f.readline().strip().split(",")

hashmap = [{} for i in range(256)]

for label in data:
    if "-" in label:
        name = label.rstrip("-")
        if name in hashmap[hash(name)]:
            hashmap[hash(name)].pop(name)
    else:
        name, value = label.split("=")
        hashmap[hash(name)][name] = int(value)

res = 0
for box, lenses in enumerate(hashmap):
    counter = 0
    for focal in lenses.values():
        counter += 1
        res += counter * focal * (box+1)
print(res)