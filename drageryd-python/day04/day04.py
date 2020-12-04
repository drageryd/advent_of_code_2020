import sys

def parse(data):
    # Parse batch file into list of dictionaries
    batch_file = []
    for passport in data.split("\n\n"):
        # Parse passport into list of entry pairs (e.g ("ecl", "gry"))
        passport = [tuple(entry.split(":")) for entry in passport.replace("\n", " ").split(" ")]
        # Append batch file with dictionary of entries (e.g {"ecl": "gry"})
        batch_file.append({k:v for k,v in passport})
    return batch_file

def byr(x):
    return int(x) >= 1920 and int(x) <= 2002

def iyr(x):
    return int(x) >= 2010 and int(x) <= 2020

def eyr(x):
    return int(x) >= 2020 and int(x) <= 2030

def hgt(x):
    if x[-2:] == "cm":
        return int(x[:-2]) >= 150 and int(x[:-2]) <= 193
    elif x[-2:] == "in":
        return int(x[:-2]) >= 59 and int(x[:-2]) <= 76
    return False

def hcl(x):
    return len(x) == 7 and x[0] == "#" and all(c in "0123456789abcdef" for c in x[1:])

def ecl(x):
    return x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def pid(x):
    return len(x) == 9 and all(c in "0123456789" for c in x)

# Required fileds (without cid)
fields = {"byr": byr, "iyr": iyr, "eyr": eyr, "hgt": hgt, "hcl": hcl, "ecl": ecl, "pid": pid}

# Parse input file
data = sys.stdin.read().strip()
batch_file = parse(data)

# Filter batch file to only contain passports with all required fields
batch_file = [p for p in batch_file if set(fields.keys()).issubset(p)]
print("Part 1: {}".format(len(batch_file)))

# Fliter all remaining to those with valid data
batch_file = [p for p in batch_file if all(check(p[f]) for f, check in fields.items())]
print("Part 2: {}".format(len(batch_file)))
