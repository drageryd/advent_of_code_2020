import sys
from functools import reduce

data = sys.stdin.read().strip().split("\n")
slopes = {(1,1):0, (3,1):0, (5,1):0, (7,1):0, (1,2):0}

for i in range(len(data)):
    for x,y in slopes:
        if i * y < len(data):
            row = data[i * y]
            if row[(i * x) % len(row)] == "#":
                slopes[(x,y)] += 1

print("Part 1: {}".format(slopes[(3,1)]))
print("Part 2: {}".format(reduce(lambda a, b: a * b, slopes.values())))
