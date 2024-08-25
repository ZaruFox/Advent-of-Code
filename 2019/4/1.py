with open("data.txt") as f:
    validRange = [int(x) for x in f.readline().strip().split("-")]

res = 0
for password in range(validRange[0], validRange[1]+1):
    password = str(password)
    doubleDigit = False
    alwaysIncreasing = True
    for i in range(1,6):
        if password[i] == password[i-1]:
            doubleDigit = True
        elif password[i] < password[i-1]:
            alwaysIncreasing = False
            break

    if alwaysIncreasing and doubleDigit:
        res += 1
print(res)