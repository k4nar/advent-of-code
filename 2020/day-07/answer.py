from collections import defaultdict


def get_bags(lines):
    bags = defaultdict(dict)

    for line in lines:
        line = line.strip()

        bag, _, line = line.partition(" bags contain ")

        if line.strip() == "no other bags.":
            continue

        for rule in line.split(","):
            number, name = rule.strip().split(" ", 1)
            number = int(number)
            name, _ = name.rsplit(" ", 1)

            bags[bag][name] = number

    return bags


with open("input") as f:
    bags = get_bags(f)

print("-" * 80)
print("Part 1")


def get_containers(bag):
    containers = set(candidate for candidate, rules in bags.items() if bag in rules)

    for bag in list(containers):
        containers |= get_containers(bag)

    return containers


containers = get_containers("shiny gold")
print(f"answer: {len(containers)}")

print("-" * 80)
print("Part 2")


def get_size(rules):
    size = 0

    for bag, nb in rules.items():
        size += nb * (get_size(bags[bag]) + 1)

    return size


size = get_size(bags["shiny gold"])
print(f"answer: {size}")
