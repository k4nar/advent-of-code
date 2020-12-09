from collections import deque
from itertools import combinations

with open("input") as f:
    numbers = [int(line.strip()) for line in f]

print("-" * 80)
print("Part 1")


def find_invalid_number(numbers, size=25):
    preamble = deque(numbers[:size], size)

    for number in numbers[size:]:
        if not any(x + y == number for x, y in combinations(preamble, 2)):
            return number

        preamble.append(number)


invalid = find_invalid_number(numbers)
print(f"answer: {invalid}")

print("-" * 80)
print("Part 2")


def find_weakness(numbers, invalid):
    for size in range(2, len(numbers)):
        for candidate in zip(*(numbers[i:] for i in range(size))):
            if sum(candidate) == invalid:
                return min(candidate) + max(candidate)


weakness = find_weakness(numbers, invalid)
print(f"answer: {weakness}")
