import math

with open("data.txt") as f:
    data = [x.strip() for x in f.readlines()]

# f(x) = ax + b mod m
# g(x) = cx + d mod m
# g(f(x)) = c(ax+b) + d mod m
#         = acx + bc + d mod m
    
# deal: f(x) = m - x - 1
#            = -x -1 mod m

# cut: f(x) = x - a mod m
    
# incre: f(x) = ax mod m
    
n = 119315717514047
cycles = 101741582076661

firstFunction = data[0]
if firstFunction == "deal into new stack":
    a = -1
    b = -1
elif firstFunction.startswith("deal with increment "):
    a = int(firstFunction.lstrip("deal with increment "))
    b = 0
else:
    a = 1
    b = -int(firstFunction.lstrip("cut "))

for line in data[1:]:
    if line == "deal into new stack":
        a *= -1
        b *= -1
        b -= 1
    elif line.startswith("deal with increment "):
        a *= int(line.lstrip("deal with increment "))
        b *= int(line.lstrip("deal with increment "))
    else:
        b -= int(line.lstrip("cut "))

    a %= n
    b %= n

# f(x) = ax + b mod m
# f^2(x) = a(ax + b) + b mod m
#        = a^2x + ab + b mod m
# f^3(x) = a(a^2x + ab + b) + b mod m
#        = a^3x + a^2b + ab + b mod m
#        = a^3x + (a^2 + a + 1) * b
# f^n(x) = a^nx + (a^(n-1) + a^(n-2) ... + a^(0)) * b mod m
finalA = pow(a, cycles, n) % n
# b = (((1 - pow(a, cycles, n))/(1-a))*b) 
# y(finalB) = x (mod n)
x = ((1 - pow(a, cycles, n)) * b) % n
y = (1-a) % n
modularInverse = pow(y, n-2, n)
finalB = (x * modularInverse) % n

# f(f^-1(x)) = x mod n
# x = a(f^-1(x)) + b mod n
# (x-b)/a = f^-1(x) mod n
# f^-1(2020)*a = 2020-b mod n

print((pow(finalA, n-2, n) * (2020 - finalB)) % n)
