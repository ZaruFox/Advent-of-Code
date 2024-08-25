with open("data.txt") as f:
    validRange = [int(x) for x in f.readline().strip().split("-")]

res = 0
for password in range(validRange[0], validRange[1]+1):
    password = str(password)
    continuous = 1
    doubleDigit = False
    alwaysIncreasing = True
    
    for i in range(1,6):
        if password[i] == password[i-1]:
            continuous += 1
        else:
            if continuous == 2:
                doubleDigit = True
            continuous = 1
        
        if password[i] < password[i-1]:
            alwaysIncreasing = False
            break

    if alwaysIncreasing and (doubleDigit or continuous == 2):
        res += 1
print(res)