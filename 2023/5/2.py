class Mapping:
    def __init__(self, desti, source, rangeLen):
        self.delta = desti-source
        self.sourceStart = source
        self.sourceEnd = source + rangeLen-1

    def convertNumber(self, number):
        """
        Takes a number and returns its converted value

        Returns -1 if not in range
        """
        if self.sourceStart <= number <= self.sourceEnd:
            return number + self.delta
        return -1

    def mapIntervals(self, intervals):
        """
        Takes a list of intervals and return a list of intervals that are changed, with the values converted, and a list of intervals that remain unchanged
        """
        changed = []
        unchanged = []
        for interval in intervals:
            start, end = interval
            # skip if no intersect
            if self.sourceStart > end or self.sourceEnd < start:
                unchanged.append(interval)
                continue

            # find the intersect of the mapping interval and the given interval
            changedInterval = (max(self.sourceStart, start), min(self.sourceEnd, end))

            # add left unchanged interval
            if changedInterval[0] != start:
                unchanged.append((start, self.sourceStart-1))

            # add right unchanged interval
            if changedInterval[1] != end:
                unchanged.append((self.sourceEnd+1, end))

            # convert the values of the changed interval
            changed.append((self.convertNumber(changedInterval[0]), self.convertNumber(changedInterval[1])))

        return unchanged, changed
            
                
            
# split and save each line into data, excluding empty lines
data = []
with open("data2.txt") as f:
    for line in f:
        if line == "\n":
            continue
        data.append(line.strip().split())

# gets the intervals of the seeds
seedsData = [int(x) for x in data[0][1:]]
intervals = [(seedsData[i], seedsData[i]+seedsData[i+1]-1) for i in range(0, len(seedsData), 2)]


allMaps = []
table = []
for i in range(3, len(data)):
    # when it is a row of a table, append a Mapping class to the list with the data in the row
    if data[i][0].isdigit():
        table.append(Mapping(*[int(x) for x in data[i]]))

    # if it is not a row of digits, it end of a table, append the completed table to the list of tables
    else:
        allMaps.append(table)
        table = []

# append the last remaining table
allMaps.append(table)

# for each table, loop through each row and apply the mapping
for table in allMaps:
    # intervals that are changed should not included in the mapping, therefore store them in a seperate list
    changedIntervals = []
    for row in table:
        intervals, changed = row.mapIntervals(intervals)
        changedIntervals += changed

    # after processing the entire table, add the changed intervals back and continue with next table 
    intervals += changedIntervals


# check the lower bounds for the minimum value
print(min([x[0] for x in intervals]))