from functools import reduce
from itertools import cycle, islice
from operator import mul

with open("input") as f:
    lines = [line.strip() for line in f.readlines()]


def nth(iterable, n):
    return next(islice(iterable, n, None))


def get_number_of_trees(right, down):
    forest = [cycle(row) for row in lines]

    trees = 0
    x, y = right, down

    while y < len(forest):
        row = forest[y]
        trees += nth(row, x) == "#"
        x += right
        y += down

    return trees


print("-" * 80)
print("Part 1")

trees = get_number_of_trees(3, 1)
print(f"Answer: {trees}")

print("-" * 80)
print("Part 2")

patterns = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
x = list(get_number_of_trees(right, down) for right, down in patterns)
trees = reduce(mul, x)

print(f"Answer: {trees}")
