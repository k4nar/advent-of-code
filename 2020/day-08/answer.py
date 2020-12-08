acc = 0


class InfiniteLoop(RuntimeError):
    pass


def get_instructions(lines):
    for line in lines:
        line = line.strip()
        instruction, _, offset = line.partition(" ")
        offset = int(offset)
        yield (instruction, offset)


with open("input") as f:
    instructions = list(get_instructions(f))


def run(instructions, raise_on_infinite_loop=True):
    acc = 0
    seen = set()
    current = 0

    while current < len(instructions):
        if current in seen:
            if raise_on_infinite_loop:
                raise InfiniteLoop()
            else:
                break
        seen.add(current)

        instruction, offset = instructions[current]
        if instruction == "nop":
            current += 1
        elif instruction == "acc":
            acc += offset
            current += 1
        elif instruction == "jmp":
            current += offset

    return acc


print("-" * 80)
print("Part 1")

answer = run(instructions, raise_on_infinite_loop=False)
print(f"answer: {answer}")

print("-" * 80)
print("Part 2")


def fix_infinite_loop(instructions):
    for i, (instruction, offset) in enumerate(instructions):
        new_instructions = list(instructions)

        if instruction == "jmp":
            new_instructions[i] = ("nop", offset)
        elif instruction == "nop":
            new_instructions[i] = ("jmp", offset)
        else:
            continue

        try:
            return run(new_instructions)
        except InfiniteLoop:
            pass


answer = fix_infinite_loop(instructions)
print(f"answer: {answer}")
