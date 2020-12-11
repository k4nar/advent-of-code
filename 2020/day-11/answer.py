from itertools import accumulate

with open("input") as f:
    room = [line.strip() for line in f]

X = len(room[0])
Y = len(room)


def get_result(get_next_room, room):
    prev_room = None

    while room != prev_room:
        prev_room = room
        room = get_next_room(room)

    return sum(seat == "#" for row in room for seat in row)


print("-" * 80)
print("Part 1")


def get_next_room_part1(room):
    def get_new_seat(x, y):
        seat = room[y][x]

        if seat == ".":
            return seat

        occupied = (
            room[j][i] == "#" if 0 <= i < X and 0 <= j < Y else 0
            for i, j in (
                (x, y - 1),
                (x, y + 1),
                (x - 1, y),
                (x + 1, y),
                (x - 1, y + 1),
                (x - 1, y - 1),
                (x + 1, y - 1),
                (x + 1, y + 1),
            )
        )

        if seat == "L" and not any(occupied):
            return "#"
        elif seat == "#" and any(acc >= 4 for acc in accumulate(occupied)):
            return "L"
        else:
            return seat

    return [[get_new_seat(x, y) for x in range(X)] for y in range(Y)]


answer = get_result(get_next_room_part1, room)
print(f"answer: {answer}")

print("-" * 80)
print("Part 2")


def get_next_room_part2(room):
    def get_new_seat(x, y):
        seat = room[y][x]

        if seat == ".":
            return seat

        occupied = (
            next((s for s in seats if s != "."), ".") == "#"
            for seats in (
                (room[i - 1][x] for i in range(y, 0, -1)),
                (room[i][x] for i in range(y + 1, Y)),
                (room[y][i - 1] for i in range(x, 0, -1)),
                (room[y][i] for i in range(x + 1, X)),
                (room[j - 1][i - 1] for i, j in zip(range(x, 0, -1), range(y, 0, -1))),
                (room[j][i - 1] for i, j in zip(range(x, 0, -1), range(y + 1, Y))),
                (room[j - 1][i] for i, j in zip(range(x + 1, X), range(y, 0, -1))),
                (room[j][i] for i, j in zip(range(x + 1, X), range(y + 1, Y))),
            )
        )

        if seat == "L" and not any(occupied):
            return "#"
        elif seat == "#" and any(acc >= 5 for acc in accumulate(occupied)):
            return "L"

        return seat

    return [[get_new_seat(x, y) for x in range(X)] for y in range(Y)]


answer = get_result(get_next_room_part2, room)
print(f"answer: {answer}")
