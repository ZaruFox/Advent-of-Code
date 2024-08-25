import z3

hailstones = []

with open("data.txt") as f:
    for line in f:
        location, velocity = [[int(y) for y in x.split(", ")] for x in line.strip().split(" @ ")]
        hailstones.append([location, velocity])


fx,fy,fz,opt = z3.Int("fx"), z3.Int("fy"), z3.Int("fz"), z3.Solver()
fdx,fdy,fdz = z3.Int("fdx"), z3.Int("fdy"), z3.Int("fdz")
for i, ((x,y,z), (dx,dy,dz)) in enumerate(hailstones[:3]):
    t = z3.Int(f"t{i}")
    opt.add(t >= 0)
    opt.add(x + dx * t == fx + fdx * t)
    opt.add(y + dy * t == fy + fdy * t)
    opt.add(z + dz * t == fz + fdz * t)
assert str(opt.check()) == 'sat'
print(opt.model().eval(fx + fy + fz))