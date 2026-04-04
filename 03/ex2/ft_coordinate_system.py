import math


def get_player_pos() -> tuple[float, float, float]:
    try:
        x, y, z = input("Enter new coordinates as floats in format 'x,y,z': ")\
            .split(",")
    except Exception:
        print("Invalid syntax")
        return get_player_pos()
    pos = []
    tmp = [x, y, z]
    for i in tmp:
        try:
            nb = float(i)
            pos.append(nb)
        except ValueError as e:
            print(f"Error on parameter {i}: {e}")
            return get_player_pos()
    return (pos[0], pos[1], pos[2])


def get_distance(pos1: tuple[float, float, float],
                 pos2: tuple[float, float, float]) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2 + (z2-z1) ** 2)


def main() -> None:
    print("=== Game Coordinate System ===")
    x, y, z = 0.0, 0.0, 0.0
    defpos = (x, y, z)
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    print(f"Distance to center: {round(get_distance(pos1, defpos), 4)}\n")
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    print(
        f"Distance between the 2 sets of coordinates:"
        f"{round(get_distance(pos1, pos2), 4)} "
    )


if __name__ == "__main__":
    main()
