with open("input") as f:
    report = [int(line) for line in f.readlines()]

for i, entry in enumerate(report):
    for other in report[i + 1:]:
        if entry + other == 2020:
            print(f"{entry} + {other} == 2020")
            print(f"Answer: {entry * other}")
