from itertools import chain


def get_groups(f):
    group = []

    for line in f:
        line = line.strip()

        if not line:
            yield group
            group = []
            continue

        group.append(line)

    yield group


with open("input") as f:
    groups = list(get_groups(f))

print("-" * 80)
print("Part 1")

answer = sum(len(set(chain(*group))) for group in groups)
print(f"answer: {answer}")

print("-" * 80)
print("Part 2")

answer = sum(len(set(group[0]).intersection(*group[1:])) for group in groups)
print(f"answer: {answer}")
