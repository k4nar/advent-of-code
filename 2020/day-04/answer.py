def get_passports(f):
    passport = {}

    for line in f:
        if line == "\n":
            yield passport
            passport = {}

        for field in line.strip().split(" "):
            if ":" not in field:
                continue
            key, value = field.split(":")
            passport[key.strip()] = value.strip()

    yield passport


def is_passport_valid(passport, check_values=True):
    mandatory = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    if not set(passport.keys()) >= mandatory:
        return False

    if not check_values:
        return True

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.

    byr = passport['byr']
    if not (byr.isnumeric() and len(byr) == 4):
        return False
    if not 1920 <= int(byr) <= 2002:
        return False

    iyr = passport['iyr']
    if not (iyr.isnumeric() and len(iyr) == 4):
        return False
    if not 2010 <= int(iyr) <= 2020:
        return False

    eyr = passport['eyr']
    if not (eyr.isnumeric() and len(eyr) == 4):
        return False
    if not 2020 <= int(eyr) <= 2030:
        return False

    hgt = passport['hgt']
    if not hgt[:-2].isnumeric():
        return False
    if hgt.endswith('cm'):
        if not 150 <= int(hgt[:-2]) <= 193:
            return False
    elif hgt.endswith('in'):
        if not 59 <= int(hgt[:-2]) <= 76:
            return False
    else:
        return False

    hcl = passport['hcl']
    if not (hcl[0] == '#' and len(hcl) == 7):
        return False
    if not all(c in '0123456789abcdef' for c in hcl[1:]):
        return False

    ecl = passport['ecl']
    if ecl not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return False

    pid = passport['pid']
    if not (pid.isnumeric() and len(pid) == 9):
        return False

    return True


print("-" * 80)
print("Part 1")

valid = 0

with open("input") as f:
    for passport in get_passports(f):
        valid += is_passport_valid(passport, check_values=False)

print(f"Answer: {valid}")

print("-" * 80)
print("Part 2")

valid = 0

with open("input") as f:
    for passport in get_passports(f):
        valid += is_passport_valid(passport)

print(f"Answer: {valid}")
