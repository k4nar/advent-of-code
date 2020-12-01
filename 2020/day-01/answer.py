with open("input") as f:
    report = [int(line) for line in f.readlines()]


print("-" * 80)
print("Part 1")

for i, entry in enumerate(report):
    for other in report[i + 1:]:
        if entry + other == 2020:
            print(f"{entry} + {other} == 2020")
            print(f"Answer: {entry * other}")

print("-" * 80)
print("Part 2")

for i, entry in enumerate(report):
    for j, second in enumerate(report[i + 1:]):
        for third in report[i + j + 2:]:
            if entry + second + third == 2020:
                print(f"{entry} + {second} + {third} == 2020")
                print(f"Answer: {entry * second * third}")
