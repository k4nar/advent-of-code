import math


def get_pos(instructions, up, down, length):
    x, y = 0, length

    for letter in instructions:
        if letter == up:
            x, y = math.ceil((x + y) / 2), y
        elif letter == down:
            x, y = x, math.floor((x + y) / 2)

    return x


def get_boarding_passes(f):
    for line in f:
        line = line.strip()
        row = get_pos(line[:7], up='B', down='F', length=127)
        col = get_pos(line[7:], up='R', down='L', length=7)
        yield row * 8 + col


with open('input') as f:
    boarding_passes = set(get_boarding_passes(f))


print("-" * 80)
print("Part 1")

print(f"answer: {max(boarding_passes)}")

print("-" * 80)
print("Part 2")

start = min(boarding_passes)
end = max(boarding_passes)
missing = [seat for seat in range(start, end) if seat not in boarding_passes]

assert len(missing) == 1

print(f"answer: {missing[0]}")
