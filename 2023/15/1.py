def hash(word):
    cur = 0
    
    for chara in word:
        cur += ord(chara)
        cur *= 17
        cur %= 256
        
    return cur
        

with open("data.txt") as f:
    data = f.readline().strip().split(",")

res = 0
for word in data:
    res += hash(word)
print(res)