import math

register1 = 0
register2 = 0
register3 = 0
register5 = 0

res = math.inf 
visited = set()


while True:
    if register3 in visited:
        break
    res = register3
    visited.add(register3)

    register5 = register3 | 65536
    register3 = 5557974
    
    while True:
        register3 += register5 % 256
        register3 = (register3 * 65899) % 16777216

        if 256 > register5:
            break
        else:
            register5 //= 256

print(res)