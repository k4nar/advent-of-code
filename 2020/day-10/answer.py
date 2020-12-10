from collections import Counter

with open("input") as f:
    adapters = sorted(int(line.strip()) for line in f)

print("-" * 80)
print("Part 1")

counter = Counter()
for x, y in zip([0, *adapters], adapters):
    counter[y - x] += 1

print(f"answer: {counter[1] * (counter[3] + 1)}")

print("-" * 80)
print("Part 2")

ways = {adapters[-1]: 1}
for x in reversed([0, *adapters[:-1]]):
    ways[x] = ways.get(x + 1, 0) + ways.get(x + 2, 0) + ways.get(x + 3, 0)

print(f"answer: {ways[0]}")
