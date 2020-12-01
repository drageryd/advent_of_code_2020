import sys
from itertools import combinations

data = sys.stdin.read().strip()
numbers = [int(row) for row in data.split("\n")]

for x, y in combinations(numbers, 2):
    if x + y == 2020:
        print("Part 1: {}".format(x * y))
        break

for x, y, z in combinations(numbers, 3):
    if x + y + z == 2020:
        print("Part 2: {}".format(x * y * z))
        break
