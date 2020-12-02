import sys

data = sys.stdin.read().strip()
# lower-upper letter: password
passwords = []
for row in data.split("\n"):
    # lower-upper letter: password
    row = row.replace(":", "")
    row = row.replace("-", " ")
    lower, upper, letter, password = row.split(" ")
    # lower and upper are integers
    lower = int(lower)
    upper = int(upper)
    # Add to parsed passwords
    passwords.append((lower, upper, letter, password))

# The count of the letter should be within lower and upper bounds
print("Part 1: {}".format(len([1 for l, u, c, p in passwords if p.count(c) >= l and p.count(c) <= u])))
# The letter should appear in only one of the locations defined by lower and upperd
print("Part 1: {}".format(len([1 for l, u, c, p in passwords if (p[l-1] == c) != (p[u-1] == c)])))
