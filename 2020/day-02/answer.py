from typing import NamedTuple


class Line(NamedTuple):
    a: int
    b: int
    letter: str
    password: str

    @classmethod
    def parse(cls, line):
        a, _, line = line.partition("-")
        b, _, line = line.partition(" ")
        letter, _, line = line.partition(":")
        password = line.strip()

        return cls(
            a=int(a),
            b=int(b),
            letter=letter,
            password=password,
        )


def get_lines():
    with open("input") as f:
        for line in f.readlines():
            yield Line.parse(line)


print("-" * 80)
print("Part 1")

correct_passwords = 0

for line in get_lines():
    if line.a <= line.password.count(line.letter) <= line.b:
        correct_passwords += 1


print(f"Answer: {correct_passwords}")

print("-" * 80)
print("Part 2")

correct_passwords = 0

for line in get_lines():
    a = (line.password[line.a - 1] == line.letter)
    b = (line.password[line.b - 1] == line.letter)
    if a ^ b:
        correct_passwords += 1

print(f"Answer: {correct_passwords}")
