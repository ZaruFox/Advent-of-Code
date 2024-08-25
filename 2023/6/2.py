import math, bisect, timeit

with open("data.txt") as f:
    time = int("".join(f.readline().strip().split()[1:]))
    record = int("".join(f.readline().strip().split()[1:]))


# binary search
def binSearchManual(time, record):
    l = 0
    r = time//2+1 if time%2==1 else time//2
    oriR = r
    while r > l:
        mid = (l+r)//2

        if (time-mid)*mid > record:
             r = mid 
        else:
             l = mid + 1
    res = (oriR-l+1)*2
    return (res+1 if time % 2 == 0 else res)

# alternatively, 
def binSearch(time, record):
    mid = time//2 if time%2==1 else time//2-1
    res = (mid - bisect.bisect_left( list(range(mid+1)), record, key= lambda x:(time-x)*x)+1)*2
    return (res+1 if time % 2 == 0 else res)


# algebra soln
def algebraSoln(time, record):
    algebra = math.ceil(0.5*(time - (time**2  - 4*record)**0.5))
    if time%2 == 0:
        res = (time//2 - algebra +1)*2
    else:
        res = (time//2 - algebra)*2 +1
    return res


# code for timing binSearch function
bin_search_time = timeit.timeit(f"binSearchManual({time}, {record})", globals=globals(), number=1)
print(f"Time taken for binSearch: {bin_search_time} seconds")

# code for timing math function
math_time = timeit.timeit(f"algebraSoln({time}, {record})", globals=globals(), number=1)
print(f"Time taken for math function: {math_time} seconds")